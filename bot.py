from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

BOT_TOKEN = "8321012082:AAGjcOJK9Z4AGda-mf_mKjCIpjP5c5f86jw"
ADMIN_ID = 8142916139

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup()
    kb.add(
        types.InlineKeyboardButton(
            text="🎰 Крутить колесо",
            web_app=types.WebAppInfo(
                url="https://axmedgoigov15-ux.github.io/telegram-wheel/"
            )
        )
    )
    await message.answer("Бот запущен ✅", reply_markup=kb)

@dp.message_handler(content_types=types.ContentType.WEB_APP_DATA)
async def webapp(message: types.Message):
    await bot.send_message(
        ADMIN_ID,
        f"Данные из WebApp:\n{message.web_app_data.data}"
    )
    await message.answer("Результат получен 👍")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
