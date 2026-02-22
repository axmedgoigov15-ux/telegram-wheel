from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

BOT_TOKEN = "8321012082:AAGjcOJK9Z4AGda-mf_mKjCIpjP5c5f86jw"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("✅ Бот успешно запущен")

if __name__ == "__main__":
    executor.start_polling(dp)
