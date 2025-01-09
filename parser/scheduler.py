from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot

from .parser import parse_data
from data.storage import get_all_chats


async def send_data(bot: Bot) -> None:
    data = parse_data()
    if data:
        chat_ids = get_all_chats()
        for chat_id in chat_ids:
            await bot.send_message(chat_id, 'Есть доступные тарифы в локации Франкфурт. 🎉')


def setup_scheduler(bot: Bot) -> None:
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_data, 'interval', hours=1, args=(bot,), next_run_time=datetime.now())
    scheduler.start()
