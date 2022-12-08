from functools import reduce

wynik = lambda a, b: a * b

print(f"Wynik mnożenia: {wynik(5, 5)}")

wiek = lambda x: "dziecko" if x < 10 else ("Nastolatek" if x < 18 else "Dorosły")

print(wiek(5))
print(wiek(15))
print(wiek(35))

lista = [1, 3, 5, 7, 9]
print(lista)

print(f"Mapowanie: {list(map(lambda x: x * 2, lista))}")
print(f"Filtrowanie: {list(filter(lambda x: x > 2, lista))}")
print(f"Redukcja: {reduce(lambda x, y: x + y, lista)}")

print(sorted("Tomek", reverse=True))
print(sorted("Tomek"))
print(sorted("Tomek", key=str.lower))

slownik = {'a': 11, 'b': 2, 'c': 0, 'd': 33}
print(sorted(slownik))
print(sorted(slownik.values()))
print(sorted(slownik.items()))
print(sorted(slownik.items(), key=lambda x: x[1]))

