import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import TOKEN
from data.storage import add_chat, init_db
from parser.scheduler import setup_scheduler

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    chat_id = message.chat.id
    add_chat(chat_id)
    await message.answer('Здравствуйте, вы зарегистрированы!')


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    setup_scheduler(bot)

    await dp.start_polling(bot)


if __name__ == '__main__':
    init_db()
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
