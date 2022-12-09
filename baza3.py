import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')

    cursor = sqliteConnection.cursor()
    print('Podłączono do bazy')

    with open('skrypt.sql', 'r') as sqlite_file:
        sql_script = sqlite_file.read()

    cursor.executescript(sql_script)

    sqliteConnection.commit()
    print('Stworzony pomyślnie tabelę w bazie')
    cursor.close()

except sqlite3.Error as error:
    print('Błąd podczas podłączenia bazy', error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("Połączenie zostało zakończone")
