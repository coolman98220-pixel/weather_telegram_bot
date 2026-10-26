from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup)

reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="погода")]
    ],
    resize_keyboard=True
)