from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
from database.bot_db import sql_command_random
from handlers.parse import parser

async def start_command(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}')


async def mem_command(message: types.Message):
    mem_photo = open("media/mem.jpg", "rb")
    await bot.send_photo(message.from_user.id, photo=mem_photo)


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("След.", callback_data='button_call_1')
    markup.add(button_1)

    question = "Кто придумал C++"
    answers = [
        'Бог',
        'Никлаус Вирт',
        'Нашальникаа',
        'Бьёрн Страуструп',
        'Никлаус Вирт',
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=3,
        explanation="ЕГО ПРИДУМАЛ САТАНА",
        open_period=30,
        reply_markup=markup
    )


async def pin(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await bot.send_message(message.chat.id, "это должно быть ответом на сообщение ")


async def get_random_mentor(message: types.Message):
    await sql_command_random(message)


async def parse_news(message: types.Message):
    items = parser()
    for item in items:
        await bot.send_message(message.chat.id,
            text=f"{item['link']}\n\n"
                 f"{item['title']}\n\n"
                 f"{item['time']}, "
                 f"#Y{item['day']}, "
                 f"#{item['year']}\n"
        )

def register_client_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(mem_command, commands=['meme'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!')
    dp.register_message_handler(parse_news, commands=['news'])
