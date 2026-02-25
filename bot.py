import json
import random
from aiogram import Bot, Dispatcher, executor, types

TOKEN = "8321012082:AAGjcOJK9Z4AGda-mf_mKjCIpjP5c5f86jw"
ADMIN_ID = 8142916139

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

USERS_FILE = "users.json"

def load_users():
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_users(data):
    with open(USERS_FILE, "w") as f:
        json.dump(data, f)

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    users = load_users()
    uid = str(msg.from_user.id)

    if uid in users:
        await msg.answer("❌ Вы уже использовали свой единственный спин.")
        return

    await msg.answer(
        "🎡 Добро пожаловать!\n\n"
        "У вас есть **1 попытка**.\n"
        "Шанс выигрыша — **1 к 1 000 000 000**.\n\n"
        "Нажмите /spin"
    )

@dp.message_handler(commands=["spin"])
async def spin(msg: types.Message):
    users = load_users()
    uid = str(msg.from_user.id)

    if uid in users:
        await msg.answer("❌ Спин уже был использован.")
        return

    users[uid] = True
    save_users(users)

    roll = random.randint(1, 1_000_000_000)

    if roll == 1:
        await msg.answer("🎉 ВЫ ВЫИГРАЛИ!\n\nОжидайте подтверждения администратора.")
        await bot.send_message(
            ADMIN_ID,
            f"🔥 ПОБЕДИТЕЛЬ!\n\n"
            f"👤 @{msg.from_user.username}\n"
            f"🆔 ID: {msg.from_user.id}\n\n"
            f"Нужно выдать приз вручную."
        )
    else:
        await msg.answer("😔 Не повезло. Это был ваш единственный спин.")

if __name__ == "__main__":
    executor.start_polling(dp)
