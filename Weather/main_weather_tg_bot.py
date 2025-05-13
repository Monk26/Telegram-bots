from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import dispatcher
from config import tg_bot_token, open_weather_token
from weather import weather

bot = Bot(token=tg_bot_token)
dp = dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши название города на английском, а я пришлю сводку погоды!")

@dp.message_handler()
async def get_weather(message: types.Message):
    city = message.text
    result = weather(city, open_weather_token)
    await message.reply(result)

if __name__ == "__main__":
    executor.start_polling(dp)