# szopy = []
# while True:
#     print(f"""
#
#         1. adoptuj szopa
#             2. pogon szopa
#                 3. wyjdz z programu
#              🦝🦝🦝 lista adoptowanych szopów:{szopy} 🦝🦝🦝
#     """)
#     wybor = input("Wybierz opcję:")
#     if wybor == "1":
#         szopy.append("Franek")
#     elif wybor == "2":
#         szopy.pop()
#     elif wybor == "3":
#         break
#     else:
#         print("Nie ma takiej opcji, sprawdź menu")
# print("Copyright by...")


# licznik = 0
# while True:
#     licznik += 1
#     print(licznik)
#     if licznik == 10:
#         break
#
# counter = 0
# while counter < 5:
#     print(counter, "mniejsze od 5")
#     counter += 1

lista = []
for i in range(1, 6, 2):
    lista.append(i)

print(lista)

for i in lista:
    print(i)

for index, wartosc in enumerate(lista):
    print(f"INDEX: {index} => WARTOŚC: {wartosc}")

for i in range(1, 10 + 1):
    for j in range(10 - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

slownik = {"imie": "Marek", "nazwisko": "Kowalski", "plec": "mezczyzna"}

for i in slownik:
    print(i)
for i in slownik.values():
    print(i)
for i, v in slownik.items():
    print(i, "->", v)
