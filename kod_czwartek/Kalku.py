class Kalkulator:
    def __init__(self, x, y):
        self.liczba1 = x
        self.liczba2 = y
        self.wynik = 0

    def dodaj(self):
        self.wynik = self.liczba1 + self.liczba2
        self.__wyswietl_wynik()

    def odejmij(self):
        self.wynik = self.liczba1 - self.liczba2
        self.__wyswietl_wynik()

    def pomnoz(self):
        self.wynik = self.liczba1 * self.liczba2
        self.__wyswietl_wynik()

    def podziel(self):
        if self.liczba2 != 0:
            self.wynik = self.liczba1 / self.liczba2
            self.__wyswietl_wynik()
        else:
            print("Nie dziel przez 0")

    def __wyswietl_wynik(self):
        print(self.wynik)


calc = Kalkulator(2, 5)
calc.podziel()
calc.dodaj()
cal2 = Kalkulator(3233, 5)
calc.podziel()
calc.odejmij()

