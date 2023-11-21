from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.row("Создать пароль")
menu.row("Цитата")
menu.row("Связь с Админом")

password_types = InlineKeyboardMarkup(row_width=1)
password_types.add(
    InlineKeyboardButton(text="Murakkab", callback_data="hard"),
    InlineKeyboardButton(text="O'rtancha", callback_data="middle"),
    InlineKeyboardButton(text="Oddiy", callback_data="easy")
)

quotes_btn = InlineKeyboardMarkup()
quotes_btn.add(
    InlineKeyboardButton(text="generate", callback_data="rand_quote")
)