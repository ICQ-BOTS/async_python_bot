import asyncio
import logging

log = logging.getLogger(__name__)


class User:
    def __init__(self, id, bot, task=None, parent_event_id=None):
        self.id = id
        self.bot = bot
        self.task = task
        self.parent_event_id = parent_event_id
        self.events = asyncio.Queue(maxsize=bot.task_max_len)
        self.handler = None

    async def wait_response(self):
        log.info(self)
        return await self.events.get()

    def __str__(self):
        return f'User(id={self.id}, parent_event_id={self.parent_event_id})'

