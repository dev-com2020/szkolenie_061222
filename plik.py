# w - zapis(NADPISANIE!)
# r - odczyt
# a - dopisanie!

lista = []
# wartosc = input("Wprowadź dane do bazy:")

# with open('baza.txt', "a", encoding="utf-8") as fh:
#     fh.write(wartosc)
#     fh.write("\n")


with open('baza.txt', "r", encoding="utf-8") as fh:
    while fh.readline() != "":
        zapis = fh.readline().rstrip()
        lista.append(zapis)


print(lista)
