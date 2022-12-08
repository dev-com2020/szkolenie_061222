class Human2:

    def __init__(self, imie: str, wiek: int, plec: str):
        """
        Klasa Human 2.0 - symuluje człowieka
        :param imie: dowolne
        :param wiek: 0 do 100
        :param plec:k lub kobieta lub cokolwiek
        """
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def przywitaj(self):
        print(f"Cześć,mam na imię {self.imie}")

    def ruszaj(self):
        if self.plec == 'k' or self.plec == 'kobieta':
            print("Ruszyłam w drogę!")
        else:
            print("Ruszyłem w drogę...")

    def licz(self, a, b):
        if self.wiek > 6:
            print("Wynik:", a + b)
        else:
            print("Ja nie umiem jeszcze liczyć!")
