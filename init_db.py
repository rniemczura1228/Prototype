import sqlite3
from datetime import datetime

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
current=datetime.now()

cur.execute("insert into posts (name, number_parts, created_date, updated_date) values (?, ?, ?, ?)",
            ('Widget-10', 10, current, current)
            )

cur.execute("insert into posts (name, number_parts, created_date, updated_date) values (?, ?, ?, ?)",
            ('Widget-20', 20, current, current)
            )

connection.commit()
connection.close()