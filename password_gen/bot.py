import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command
from btn import *
from string import ascii_letters
from random import choice
import aiohttp

logging.basicConfig(level=logging.INFO)

quotes_api = "https://zenquotes.io/api/quotes"

BOT_TOKEN = "6306000460:AAETRQkjNRl_mdOFmuXwKaaacfbil6NxY90"


bot = Bot(token=BOT_TOKEN, parse_mode="html")
dp = Dispatcher(bot=bot)


async def set_my_bot_commands(dp: Dispatcher):
   await dp.bot.set_my_commands([
  types.BotCommand("start", "Start bot"),
  types.BotCommand("generate", "Generate Password"),
])
   
letters = ascii_letters
symbols = "!@#$%^&*()_+:='"
numbers = "1234567890"


async def generate_password(level: str):
    password = ""
    if level == "hard":
        for item in range(4):
            password += choice(letters) + choice(symbols) + choice(numbers)
    elif level == "middle":
        for item in range(6):
            password += choice(letters) + choice(numbers)
    else:
        for item in range(8):
            password += choice(numbers)
    
    return password


async def get_quotes():
   async with aiohttp.ClientSession() as session:
      async with session.get(quotes_api) as response:
         return await response.json()
    


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
  await message.answer("Salom", reply_markup=menu)


@dp.message_handler(text='Создать пароль')
async def generate_password_handler(message: types.Message):
  await message.answer("Связь с Админом: ", reply_markup=password_types)


@dp.message_handler(text='Цитата')
async def generate_password_handler(message: types.Message):
  await message.answer("Нажмите на кнопку: ", reply_markup=quotes_btn)


@dp.callback_query_handler(text="rand_quote")
async def random_quote_call(call: types.CallbackQuery):
   quote = await get_quotes()
   result = choice(quote)['q']
   await call.message.edit_text(f"<b>Цитата</b>:\n<em>{result}</em>", reply_markup=quotes_btn)


@dp.callback_query_handler()
async def hard_password_handler(call: types.CallbackQuery):
  level = call.data
  password = await generate_password(level=level)
  await call.message.edit_text(f"<b>Parol:</b> <code>{password}</code>", reply_markup=password_types)


@dp.message_handler(text="Admin bilan bog'lanish")
async def admin_hand(message: types.Message):
   await message.reply("<b>🚦Здарова\n📞Это список наших Админов\nСоздатель: @S1mple_T</b>\n<b>Гл.Админ</b>: @diyor12a\n🧨<ins>Писать только по проблемам или по Запросам\nПо другим делам не писать или сразу спам!!!</ins>")






if __name__ == "__main__":
 executor.start_polling(dp, on_startup=set_my_bot_commands)
