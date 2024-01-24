import sqlite3 as sq

db = sq.connect('tg.db')
cur = db.cursor()


async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS accounts_user("
                "user_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "cart_id TEXT, "
                "sells_count INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS items("
                "i_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "name TEXT,"
                "taste TEXT,"
                "price INTEGER )")
    db.commit()