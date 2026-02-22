from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# === ТВОИ ДАННЫЕ ===
BOT_TOKEN = "8321012082:AAGjcOJK9Z4AGda-mf_mKjCIpjP5c5f86jw"
ADMIN_ID = 8142916139  # твой Telegram ID

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        "🎡 Добро пожаловать!\n\n"
        "Нажми кнопку ниже, чтобы крутить колесо 👇",
        reply_markup=types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton(
                text="🎰 Крутить колесо",
                web_app=types.WebAppInfo(
                    url="https://axmedgoigov15-ux.github.io/telegram-wheel/"
                )
            )
        )
    )

@dp.message_handler(content_types=types.ContentType.WEB_APP_DATA)
async def web_app_data(message: types.Message):
    data = message.web_app_data.data

    # уведомление админу
    await bot.send_message(
        ADMIN_ID,
        f"🎯 РЕЗУЛЬТАТ СПИНА\n"
        f"Пользователь: @{message.from_user.username}\n"
        f"ID: {message.from_user.id}\n"
        f"Данные: {data}"
    )

    await message.answer(
        "⏳ Результат зафиксирован.\n"
        "Если это выигрыш — администратор свяжется с тобой."
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
