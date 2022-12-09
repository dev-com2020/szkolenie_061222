import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')

    cursor = sqliteConnection.cursor()
    print('Podłączono do bazy')

    sqlite_insert = '''INSERT INTO software(id,name,price) VALUES (1,'Pycharm',1000)'''

    sqliteConnection.execute(sqlite_insert)
    sqliteConnection.commit()
    print('Stworzony pomyślnie tabelę w bazie')
    cursor.close()

except sqlite3.Error as error:
    print('Błąd podczas podłączenia bazy', error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("Połączenie zostało zakończone")
