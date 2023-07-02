from aiogram import Bot, Dispatcher, types, executor

import config
from keyboards import markup, markup2
import database as db

bot = Bot(config.bot_token)
dp = Dispatcher(bot=bot)


async def on_startup(_):
    await db.db_start()
    print("Запущен")

@dp.message_handler(commands=['start'])
async def command_start(msg: types.Message):
    await db.cmd_start_db(msg.from_user.id)
    await msg.answer('Welcome to the Official TGBot TSPA!', reply_markup=markup)


@dp.callback_query_handler()
async def callback_query_keyboad(callback_query: types.CallbackQuery):
    if callback_query.data == "spa":
        await bot.send_message(chat_id=callback_query.from_user.id, text='Welcome to the TSPA!', reply_markup=markup2)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
