import sqlite3 as sq

db = sq.connect('tg.db')
cur = db.cursor()


async def db_start():
    #ПОМЕНЯТЬ
    cur.execute("CREATE TABLE IF NOT EXISTS accounts_user("
                "user_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "tg_id INTEGER, "
                "cart_id TEXT, "
                "sells_count INTEGER)")

    cur.execute("CREATE TABLE IF NOT EXISTS yz("
                "tg_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "name TEXT,"
                "dop_name TEXT,"
                "count INTEGER,"
                "sells_count INTEGER)")

    cur.execute("CREATE TABLE IF NOT EXISTS novovyatsk("
                "tg_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "name TEXT,"
                "dop_name TEXT,"
                "count INTEGER,"
                "sells_count INTEGER)")

    cur.execute("CREATE TABLE IF NOT EXISTS cym("
                "tg_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "name TEXT,"
                "dop_name TEXT,"
                "count INTEGER,"
                "sells_count INTEGER)")

    cur.execute("CREATE TABLE IF NOT EXISTS every_day_catalog("
                "№ INTEGER PRIMARY KEY AUTOINCREMENT,"
                "name TEXT , "
                "count INTEGER,"
                "price INTEGER,"
                "sum INTEGER )")

    cur.execute("CREATE TABLE IF NOT EXISTS catalog("
                "№ INTEGER PRIMARY KEY AUTOINCREMENT,"
                "name TEXT , "
                "count INTEGER,"
                "price INTEGER,"
                "sum INTEGER )")
    db.commit()


async def cmd_db_start(user_id):
    user = cur.execute("SELECT * FROM accounts_user WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO accounts_user (tg_id) VALUES ({key})".format(key=user_id))
        db.commit()