import pandas as pd

# print(pd.read_excel('imiona.xlsx'))

slownik = {"Imie": ['Monika', "Karol", "Tomek"], 'wiek': [19, 22, 25]}
lista = [[1, 25, 7, 66], [54, 23, 3, 88]]
zbior = pd.DataFrame(slownik)
# zbior.columns = ['Jeden', "Dwa", "Trzy", 'Cztery']
print(zbior)

# zbior.to_xml('dane_z_pandas.xml')
