import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    sqlite_create_table = ''' CREATE TABLE SqliteDb_developers (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            email text NOT NULL UNIQUE,
                            joining_date datetime,
                            salary REAL NOT NULL);'''

    cursor = sqliteConnection.cursor()
    print('Podłączono do bazy')

    cursor.execute(sqlite_create_table)
    sqliteConnection.commit()
    print('Stworzony pomyślnie tabelę w bazie')
    cursor.close()

except sqlite3.Error as error:
    print('Błąd podczas podłączenia bazy', error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("Połączenie zostało zakończone")
