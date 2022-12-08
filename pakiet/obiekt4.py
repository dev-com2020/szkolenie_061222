class Tesla:
    def __init__(self, kolor='biały'):
        self.silnik = False
        self.bieg = 0
        self.predkosc = 0
        self.kolor = kolor

    def uruchom(self):
        self.silnik = True

    def wylacz(self):
        self.silnik = False

    def biegNastepny(self):
        if self.bieg <= 6:
            self.bieg += 1
            print(f"Bieg:{self.bieg}")

    def biegPoprzedni(self):
        if self.bieg >= 0:
            self.bieg -= 1
            print(f"Bieg:{self.bieg}")

    def przyspiesz(self):
        if self.silnik == True and self.bieg > 0:
            self.predkosc += 10
            print(f"Prędkość:{self.predkosc}")

    def hamuj(self):
        if self.predkosc >= 10:
            self.predkosc -= 10
            print(f"Prędkość:{self.predkosc}")
        else:
            self.predkosc = 0
