from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

if __name__ == '__main__':
    executor.start_polling(dp)
