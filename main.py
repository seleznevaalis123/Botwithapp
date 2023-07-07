from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import config
from keyboards import markup, markup2, markup3, markup4
import database as db


bot = Bot(config.bot_token)
dp = Dispatcher(bot=bot)


async def on_startup(_):
    await db.db_start()
    print("started")


@dp.message_handler(commands=['start'])
async def command_start(msg: types.Message):
    await db.cmd_start_db(msg.from_user.id)
    await bot.send_photo(chat_id=msg.chat.id,
                         photo='https://avatars.mds.yandex.net/get-altay/1868686/2a0000016a0afc45ddadefd260492d2a734a/orig',
                         caption='Welcome to the Official TGBot TSPA! Experience the ultimate luxury spa experience at Jaens'
                                 ' Spa Ubud, with a unique combination of a traditional Balinese spa combined with modern'
                                 ' facilities and treatments.',
                         reply_markup=markup)


@dp.callback_query_handler()
async def callback_query_keyboad(callback_query: types.CallbackQuery):
    if callback_query.data == "spa":
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        await bot.send_photo(chat_id=callback_query.from_user.id,
                             photo='https://www.realbali.com/wp-content/uploads/2013/11/bali-massage-for-couple.jpg',
                             caption='Soak up panoramic views across the Petanu River gorge at the beautiful Lembah Spa. Boasting one of the most tranquil settings and renowned for being one of the best spas in Bali, Lembah spa is the perfect location to take care of your mind, body and soul. Lembah Spa’s menu contains a specialty mix of western and traditional Balinese wellness treatments – guaranteed to place your body in a pure state of relaxation.!',
                             reply_markup=markup2)

    elif callback_query.data == "main menu":
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        await bot.send_photo(chat_id=callback_query.from_user.id,
                             photo='https://avatars.mds.yandex.net/get-altay/1868686/2a0000016a0afc45ddadefd260492d2a734a/orig',
                             caption='Welcome to the Official TGBot TSPA! '
                                     'Experience the ultimate luxury spa experience at Jaens Spa Ubud, with a unique combination of '
                                     'a traditional Balinese spa combined with modern facilities and treatments.',
                             reply_markup=markup)
    elif callback_query.data == 'spa menu':
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        await bot.send_photo(chat_id=callback_query.from_user.id,
                             photo='https://www.flokq.com/blog/wp-content/uploads/2021/01/5-bali-spa-800x600.jpg',
                             caption='Ꮥelect category💫',
                             reply_markup=markup3)
    elif callback_query.data == 'back_spa':
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        await bot.send_photo(chat_id=callback_query.from_user.id,
                             photo='https://www.realbali.com/wp-content/uploads/2013/11/bali-massage-for-couple.jpg',
                             caption='Soak up panoramic views across the Petanu River gorge at the beautiful Lembah Spa. Boasting one of the most tranquil settings and renowned for being one of the best spas in Bali, Lembah spa is the perfect location to take care of your mind, body and soul. Lembah Spa’s menu contains a specialty mix of western and traditional Balinese wellness treatments – guaranteed to place your body in a pure state of relaxation.!',
                             reply_markup=markup2)
    elif callback_query.data == 'massage menu':
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        await db.sql_read_one(callback_query)
        await bot.send_message(chat_id=callback_query.from_user.id, text="You can go back to categories!💎",
                               reply_markup=markup4)
    elif callback_query.data == 'scrub':
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        await db.sql_read_two(callback_query)
        await bot.send_message(chat_id=callback_query.from_user.id, text="You can go back to categories!💎",
                               reply_markup=markup4)
    elif callback_query.data == '️back_spa_menu':
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        await bot.send_photo(chat_id=callback_query.from_user.id,
                             photo='https://www.flokq.com/blog/wp-content/uploads/2021/01/5-bali-spa-800x600.jpg',
                             caption='Ꮥelect category💫',
                             reply_markup=markup3)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
