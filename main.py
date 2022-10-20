
from aiogram.utils import executor
from config import dp
import logging
from handlers import client, call_back, extra, FSMAdminmentor, admin
from database.bot_db import sql_create


async def on_startup(_):
    sql_create()


admin.register_handlers_admin(dp)
client.register_client_handlers(dp)
call_back.register_handlers_callback(dp)
FSMAdminmentor.register_handlers_fsmadmin(dp)
extra.register_extra_handlers(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
