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
        try:
            print("Wynik dzielenia:", a / b)
        except ZeroDivisionError:
            print("Błąd dzielenia przez 0")

    def pomnoz(self, a, b):
        try:
            return int(a) * int(b)
        except TypeError:
            return "błąd typu"
        except ValueError:
            return "błąd wartości"

    def pomnoz2(self, a, b):
        try:
            return int(a) * int(b)
        except Exception as e:
            print(f"Błąd: {e.args}")


kalkulator = Kalkulator()
print(kalkulator.pomnoz('a', 'b'))
kalkulator.pomnoz2("a","b")
kalkulator.dodaj(2, 3)
kalkulator.odejmij(3, 2)
kalkulator.podziel(3, 0)
kalkulator.podziel(32, 2)

