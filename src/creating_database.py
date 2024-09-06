import sqlite3

connection = sqlite3.connect("users.db")

cur = connection.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
         password TEXT NOT NULL)
''')
connection.close()