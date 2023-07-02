import asyncio
from aiogram import Bot, Dispatcher, types, executor
import config
from keyboards import markup

bot = Bot(config.bot_token)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def command_start(msg: types.Message):
    await msg.answer('Welcome to the Official TGBot TSPA!', reply_markup=markup)


if __name__ == "__main__":
    executor.start_polling(dp)


