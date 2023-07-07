import sqlite3 as sq
from aiogram import Bot
import config

db = sq.connect('tg.db')
cur = db.cursor()
bot = Bot(config.bot_token)


async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS accounts("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "tg_id INTEGER, "
                "cart_id TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS spaitems("
                "i_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "name TEXT, "
                "desc TEXT, "
                "price TEXT, "
                "photo BLOB, "
                "brand TEXT) ")
    db.commit()
    cur.execute("INSERT INTO spaitems (name, desc, price, photo) VALUES ('face massage', 'face massage', 20,?)",
                [sq.Binary(open('photo/facemassage.jpg', 'rb').read())])



async def cmd_start_db(user_id):
    user = cur.execute("SELECT * FROM accounts WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO accounts (tg_id) VALUES ({key})".format(key=user_id))
        db.commit()


async def sql_read_one(callback_query):
    for row in cur.execute("SELECT * FROM spaitems where i_id IN (3,4)").fetchall():
        await bot.send_photo(callback_query.from_user.id, row[4], f'\nНазвание: {row[1]}\nОписание: {row[2]}\nЦена: {row[3]}')


async def sql_read_two(callback_query):
    for row in cur.execute("SELECT * FROM spaitems where i_id=1").fetchall():
        await bot.send_photo(callback_query.from_user.id, row[4], f'\nНазвание: {row[1]}\nОписание: {row[2]}\nЦена: {row[3]}')

