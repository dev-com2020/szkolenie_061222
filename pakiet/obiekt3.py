from abc import ABC, abstractmethod


class Ptak(ABC):

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lataj(self):
        print(f'tutaj {self.gatunek}, zaraz polecę z prędkością {self.szybkosc}')

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def lataj(self):
        print(f'tutaj {self.gatunek}, ja nie latam!!!')

    def wydaj_odglos(self):
        print("kokokokok")


class Orzel(Ptak):
    def poluj(self):
        print(f'tutaj {self.gatunek}, rozpoczynam polowanie!')

    def wydaj_odglos(self):
        print("piiiiii")

class Sokol(Orzel):
    def wydaj_odglos(self):
        print("piiiiiuuuuuu")