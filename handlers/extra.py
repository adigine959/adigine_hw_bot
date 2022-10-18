from aiogram import types, Dispatcher

from config import bot
import random

async def echo(message: types.Message):
    game_list = ['⚽', '🏀', '🎲', '🎰', '🎯', '🎳']
    ran = random.choice(game_list)
    if message.text.startswith('game'):
        await bot.send_dice(message.chat.id, emoji=ran)
    else:
        await bot.send_message(message.from_user.id, message.text)


def register_extra_handlers(dp: Dispatcher):
    dp.register_message_handler(echo)
