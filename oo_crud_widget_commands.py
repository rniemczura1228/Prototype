import sqlite3
from datetime import datetime

def insert_widget(id, name, number_parts, created_date, updated_date):
    try:
        sqliteConnection = sqlite3.connect('oo_database.db')
        cursor = sqliteConnection.cursor()
        sqlite_insert_with_param = """INSERT INTO widget
                          (id, name, number_parts, created_date, updated_date) 
                          VALUES (?, ?, ?, ?, ?);"""

        data_tuple = (id, name, number_parts, created_date, updated_date)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()

def readSqliteTable():
    # display widgets in sqllte atabase
    try:
        sqliteConnection = sqlite3.connect('oo_database.db')
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT * from widget"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for row in records:
            print("Id: ", row[0], " Name: ", row[1], " Number Parts: ", row[2]," Created Date: ", row[3]," Updated Date: ", row[4])

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()

def update_widget(id,name,up_date):
    # update widgets in sqlite database
    try:
        sqliteConnection = sqlite3.connect('oo_database.db')
        cursor = sqliteConnection.cursor()

        sql_update_query = """update widget set name = ?, updated_date = ? where id = ?"""
        data = (name,up_date,id)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()

def delete_widget(id):
    # delete widgets in sqlite database
    try:
        sqliteConnection = sqlite3.connect('oo_database.db')
        cursor = sqliteConnection.cursor()

        sql_update_query = """delete from widget where id=?"""
        cursor.execute(sql_update_query, (id,))
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()

def main():
#   Add Widgets
    cr_date = datetime.now()
    up_date = cr_date
    insert_widget(1, 'widget-1', 10, cr_date, up_date)
    insert_widget(2, 'widget-2', 20, cr_date, up_date)
    insert_widget(3, 'widget-3', 30, cr_date, up_date)
    print("---------------------------")
    print("Widgets after Initial Add")
    readSqliteTable()
    print("---------------------------")

#   Update Widgets
    up_date = datetime.now()
    update_widget(2, 'updated-widget-2', up_date)
    print("Widgets after Update")
    readSqliteTable()
    print("---------------------------")

#   Delete Widget
    delete_widget(3)
    print("Widgets after Delete")
    readSqliteTable()
    print("---------------------------")

if __name__ == '__main__':
    main()