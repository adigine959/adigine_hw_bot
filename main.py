import asyncio
from aiogram.utils import executor
from config import dp
import logging
from handlers import client, call_back, extra, FSMAdminmentor, admin, notifications, inline
from database.bot_db import sql_create


async def on_startup(_):
    asyncio.create_task(notifications.scheduler())
    sql_create()

inline.inline_google_handler(dp)
notifications.register_handlers_notifications(dp)
admin.register_handlers_admin(dp)
client.register_client_handlers(dp)
call_back.register_handlers_callback(dp)
FSMAdminmentor.register_handlers_fsmadmin(dp)
extra.register_extra_handlers(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
