class Human:
    """
    Klasa Human - symuluje człowieka
    """

    imie = ""
    wiek = None
    plec = ""

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
