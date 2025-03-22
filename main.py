
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message


logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] #%(levelname)-8s %(filename)s:"
    "%(lineno)d - %(name)s - %(message)s"
)

bot = Bot(token="7212828628:AAHQxwFP1uFQfr9rszk_B3X10zJgJ9Mj7v4")
dp = Dispatcher()


@dp.message(CommandStart())
async def msg(message: Message):
    await message.answer("Hello")


if __name__ == "__main__":
    dp.run_polling(bot)
