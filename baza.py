import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print('Baza danych została stworzona')

    sqlite_select_query = 'select sqlite_version();'
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print('SQLite Database version:', record)
    cursor.close()
except sqlite3.Error as error:
    print('Błąd podczas podłączenia bazy', error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("Połączenie zostało zakończone")
