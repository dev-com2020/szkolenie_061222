# class Kalkulator:
#
#     def dodaj(self, a: int, b: int):
#         wynik = a + b
#         print(wynik)
#
#     def odejmij(self, a: int, b: int):
#         wynik = a - b
#         print(wynik)
#
#     def pomnoz(self, a: int, b: int):
#         wynik = a * b
#         print(wynik)
#
#     def podziel(self, a: int, b: int):
#         wynik = a / b
#         print(wynik)
#
#
# oblicz = Kalkulator()
#
# oblicz.dodaj(4, 2)
# oblicz.odejmij(4, 2)
# oblicz.pomnoz(4, 2)
# oblicz.podziel(4, 0)
#

class Kalkulator:
    a = 0
    b = 0

    def dodaj(self, a, b):
        print("Wynik dodawania:", a + b)

    def odejmij(self, a, b):
        print("Wynik odejmowania:", a - b)

    def podziel(self, a, b):
        print("Wynik dzielenia:", a / b)

    def pomnoz(self, a, b):
        print("Wynik mnożenia:", a * b)


kalkulator = Kalkulator()
kalkulator.dodaj(2, 3)
kalkulator.odejmij(3, 2)
kalkulator.podziel(3, 0)
kalkulator.pomnoz(3, 2)
