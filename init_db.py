import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("insert into posts (name, number_parts, created_date, updated_date) values (?, ?, ?, ?)",
            ('Widget-10', 10, '1/1/2021', '1/1/2021')
            )

cur.execute("insert into posts (name, number_parts, created_date, updated_date) values (?, ?, ?, ?)",
            ('Widget-20', 20, '2/1/2021', '2/1/2021')
            )

connection.commit()
connection.close()