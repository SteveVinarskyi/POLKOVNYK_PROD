import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart
import logging

# Увімкнення логування
logging.basicConfig(level=logging.INFO)

# Замініть на ваш власний токен бота
API_TOKEN = '8159114217:AAGy998NLzmO2bWs4xmRXJAhL1D5ecIX5wg'

# Ініціалізація бота і диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def send_welcome(message: Message):
    await message.answer("Вітаю! Я бот продслужби. Надішли команду /menu для перегляду меню.")

@dp.message(lambda message: message.text.lower() == "/menu")
async def send_menu(message: Message):
 await message.reply("""Меню на день згідно з нормою №1:
1. Каша гречана
2. М'ясо тушковане
3. Хліб""")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())