from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

TOKEN = os.getenv("BOT_TOKEN") 8321012082:AAGjcOJK9Z4AGda-mf_mKjCIpjP5c5f86jwlway
ADMIN_ID = 123456789  @opportunity777bot

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(
            "🎡 Крутить колесо",
            web_app=types.WebAppInfo(url="https://ТВОЙ_НИК.github.io/telegram-wheel/")
        )
    )
    await msg.answer("Жми кнопку 👇", reply_markup=keyboard)

@dp.message_handler(commands=["win"])
async def win(msg: types.Message):
    if msg.from_user.id == ADMIN_ID:
        await msg.answer("🎉 Вы выдали выигрыш пользователю")
    else:
        await msg.answer("⛔ Только администратор")

if __name__ == "__main__":
    executor.start_polling(dp)
