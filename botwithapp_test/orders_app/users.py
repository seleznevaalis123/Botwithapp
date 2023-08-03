import psycopg2


db = psycopg2.connect(dbname='test', host='localhost', port="5432", user='selezneva', password='F8K-sRH-hR9-ASS')
cur = db.cursor()


async def cmd_start_db(user_id):
    user = cur.execute("SELECT * FROM users WHERE tg_id={key}".format(key=user_id))
    return bool(len(cur.fetchall()))

    if not user:
        cur.execute("INSERT INTO users (tg_id) VALUES ({key})".format(key=user_id))
        db.commit()