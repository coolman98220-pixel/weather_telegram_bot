from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import F, Router

from weather_parser.current_parser import get_weather
from app.keyboards import reply_keyboard


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f"Привет {message.from_user.first_name}! \n"
                        "что бы узнать погоду напиши 'погода'")

@router.message(F.text)
async def tell_weather(message: Message):
    if message.text.lower() == 'погода':
        weather = get_weather()
        await message.answer(f"Температура сейчас в Кургане: {weather['temperature']} °С\nСкорость ветра: {weather['windspeed']} м/с\n\n{weather['weathercode']}\n{weather['is_day']}",
                             reply_markup=reply_keyboard)      
    else:
        await message.reply("Извини, такой команды я не знаю. Попробуй написать 'погода'")
