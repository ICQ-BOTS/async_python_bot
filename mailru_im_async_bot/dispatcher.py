import asyncio
from mailru_im_async_bot import log
from mailru_im_async_bot.handler import DefaultHandler
from mailru_im_async_bot.user import User


class Dispatcher:
    def __init__(self, bot):
        self.bot = bot
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def remove_handler(self, handler):
        if handler in self.handlers:
            self.handlers.remove(handler)

    async def task_handler(self, handler, event, user):
        try:
            log.info(f'create task with timeout for user[{user}] event[{event.id}]')
            await asyncio.wait_for(handler.handle(event, self, user), timeout=self.bot.task_timeout_s)
        except asyncio.TimeoutError:
            log.info("task for user[{user_id}] with eventId[{event_id}] cancelled by timeout ({s})s".format(
                user_id=user.id, event_id=event.id, s=self.bot.task_timeout)
            )
        except asyncio.CancelledError:
            log.info(f"task for user[{user.id}] with eventId[{event.id}] cancelled'")
        except Exception as e:
            log.exception(e)
        finally:
            log.info(f'finally task for {user}')
            user.handler = None
            while not user.events.empty():
                remaining_event = await user.events.get()
                log.info(f'move event {remaining_event.id} from user[{user.id}] queue into bot queue')
                await self.bot.events.put(remaining_event)

    async def dispatch(self):
        while self.bot.is_running and self.bot.is_polling:
            task_len = len(asyncio.Task.all_tasks())
            if task_len < self.bot.task_max_len:
                # get event from queue
                event = await self.bot.events.get()

                # prepare user data
                user_id = event.data.get('from', {}).get('userId', None)
                if not user_id:
                    user_id = event.data.get('from', {}).get('chatId')

                user = self.bot.users.get(user_id, User(user_id, self.bot))
                self.bot.users[user_id] = user

                try:
                    log.info(f"dispatching event[{event.id}]")
                    processed = False
                    for handler in (h for h in self.handlers if h.check(event=event, dispatcher=self)):
                        log.info(f'handle event[{event.id}] by handler[{handler}]')
                        if user.task and not user.task.done():
                            if isinstance(handler, DefaultHandler) or [
                                i for i in handler.ignore if i is user.handler
                            ]:
                                log.info(f"handler[{handler}] was cancelled because user[{user}] have active task")
                                break
                            else:
                                try:
                                    log.info(f'attempt cancel user {user_id} task')
                                    user.handler = None
                                    user.task.cancel()
                                    await user.task
                                except Exception as e:
                                    log.info(e)
                        if handler.multiline:
                            user.task = self.bot.loop.create_task(self.task_handler(handler, event, user))
                            user.parent_event_id = event.id
                            user.handler = handler
                        else:
                            log.info(f'create task for user[{user}]')
                            self.bot.loop.create_task(handler.handle(event, self))
                        processed = True
                    if not processed and user.task and not user.task.done():
                        log.info(f'put event[{event.id}] into user[{user_id}] queue')
                        await self.bot.users[user_id].events.put(event)
                except StopDispatching:
                    log.debug("Caught '{}' exception, stopping dispatching.".format(StopDispatching.__name__))
                except Exception:
                    log.exception("Exception while dispatching event!")
            else:
                log.critical('task limit was reached: {}'.format(task_len))
                await asyncio.sleep(1)


class StopDispatching(Exception):
    """ If raised from handler 'check' or 'handle' methods then dispatching will be stopped. """
    pass
