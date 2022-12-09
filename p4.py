import pandas as pd

df = pd.DataFrame({"Osoba": ['Maciej Wilk', 'Marcin Onderka', 'Grażyna Sylwestrzak'], 'Wynik': [22, 34, 55]})


# print(df)

def sprawdz(punkty):
    if punkty > 25:
        return 'Zdany'
    else:
        return 'Oblany'


def rozdziel(wiersz):
    wiersz['Imie'], wiersz['Nazwisko'] = wiersz['Osoba'].split(" ")
    return wiersz


def zamien(wartosc):
    if wartosc == 'No':
        return False
    if wartosc == 'Yes':
        return True


# df.Wynik = df.Wynik.apply(sprawdz)
# df = df.apply(rozdziel, axis=1)
# # print(df.Wynik)
# print(df)


film = pd.read_csv('film.csv',
                   sep=';',
                   encoding='ISO-8859-1',
                   skiprows=[1],
                   dtype={'Length': 'float64'},
                   usecols=['Year', 'Length', 'Title', 'Subject', 'Popularity', 'Awards'],
                   converters={'Awards': lambda x: True if x == 'Yes' else False}
                   )

# print(film.groupby(['Year', 'Title']).Length.mean())
# print(film.groupby('Year').agg({'Popularity': ['min', 'max'], 'Length': ['min', 'max']}))
# print(
#     film.groupby('Year').agg(minimalna_popularność=('Popularity', 'min'), maksymalna_popularność=('Popularity', 'max')))
# print(film.info())
# film['Year'] = pd.to_numeric(film.Year)
# print(film[(film['Year'] >= 1980) & (film['Year'] <= 1990)].groupby('Year').Length.mean())

# print(film.groupby(['Year', 'Title']).agg(avg_pop=('Popularity', 'mean')).to_excel('baza_f.xlsx'))

# x = film.groupby(['Year', 'Subject']).agg(avg_pop=('Popularity', 'mean'))
# x.unstack().to_excel('baza_un.xlsx')
#
# pd.pivot_table(film,
#                index='Year',
#                columns='Subject',
#                values='Popularity',
#                aggfunc='mean')

