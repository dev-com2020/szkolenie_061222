import sqlite3


def readSqlite():
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db', timeout=20)

        cursor = sqliteConnection.cursor()
        print('Podłączono do bazy')

        sqlite_select = "SELECT * FROM software"


        sqliteConnection.execute(sqlite_select)


        for row in sqliteConnection.execute(sqlite_select):
            print(row)

        cursor.close()

    except sqlite3.Error as error:
        print('Błąd podczas podłączenia bazy', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("Połączenie zostało zakończone")


readSqlite()
