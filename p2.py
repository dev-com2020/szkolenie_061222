import pandas as pd

# s = pd.Series([11, 22, 33, 44])
# print(s)

# print(pd.read_excel('imiona.xlsx', sheet_name='Wynik2', header=None,
#                     names=['imie', 'nazwisko', 'wynik']))

miasta = pd.read_csv('worldcities.csv')
# print(miasta.head())
# print(miasta.tail())
# print(miasta[['city', 'iso2']])
# print(miasta[:20][['iso2']])
# miasta.to_excel('baza_miasta.xlsx')
# print(miasta.shape)
# print(miasta.info())
# print(miasta.id.describe())
# print(miasta.isnull().sum())
# print(miasta.notnull().sum())
print(miasta.duplicated().sum())
miasta.drop_duplicates()
# miasta.to_excel('baza_miasta.xlsx')