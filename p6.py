import pandas as pd
import sqlite3

# film = pd.read_csv('film.csv',
#                    sep=';',
#                    encoding='ISO-8859-1',
#                    skiprows=[1],
#                    dtype={'Length': 'float64'},
#                    usecols=['Year', 'Length', 'Title', 'Subject', 'Popularity', 'Awards'],
#                    converters={'Awards': lambda x: True if x == 'Yes' else False}
#                    )

conn = sqlite3.connect('baza_filmy.db')
# film.to_sql('filmy', conn)
movies = pd.read_sql("SELECT * FROM filmy WHERE Year > 1995", conn)
print(movies)
