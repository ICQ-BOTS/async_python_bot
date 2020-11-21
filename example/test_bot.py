from handlers import *
from mailru_im_async_bot.bot import Bot
from mailru_im_async_bot.handler import MessageHandler, CommandHandler, DefaultHandler, BotButtonCommandHandler
from mailru_im_async_bot.filter import Filter
from logging.config import fileConfig
from pid import PidFile
import configparser
import asyncio
import logging
import sys
import os


# Set default config path
configs_path = os.path.realpath(os.path.dirname(sys.argv[0])) + "/"

# Check exists config
if not os.path.isfile(os.path.join(configs_path, "logging.ini")):
    raise FileExistsError(f"File logging.ini not found in path {configs_path}")

# Read config
config = configparser.ConfigParser()
config.read(os.path.join(configs_path, "config.ini"))
fileConfig(os.path.join(configs_path, "logging.ini"), disable_existing_loggers=False)
log = logging.getLogger(__name__)
loop = asyncio.get_event_loop()

NAME = "TestBot"
TOKEN = '***.**********.**********:*********'

bot = Bot(token=TOKEN, name=NAME)

# Register your handlers here
# ---------------------------------------------------------------------
bot.dispatcher.add_handler(
    MessageHandler(
        multiline=True,
        callback=hello_cb,
        filters=Filter.text(['Ghbdtn', 'Привет', 'Прив', 'Хай'])
    )
)
bot.dispatcher.add_handler(
    MessageHandler(
        callback=buttons_get_cb,
        filters=Filter.regexp('(?i)кнопки'), #Regular expression
    )
)
bot.dispatcher.add_handler(CommandHandler(callback=buttons_get_cb, command='button'))#/button 
bot.dispatcher.add_handler(BotButtonCommandHandler(callback=buttons_answer_cb))

with PidFile(NAME):
    try:
        loop.create_task(bot.start_polling())
        loop.run_forever()
    except KeyboardInterrupt:
        loop.close()
    finally:
        loop.close()
