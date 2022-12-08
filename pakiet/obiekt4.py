class Tesla:
    def __init__(self, kolor='biały'):
        self.__silnik = False
        self.__bieg = 0
        self.__predkosc = 0
        self.kolor = kolor

    def uruchom(self):
        self.__silnik = True

    def wylacz(self):
        self.__silnik = False

    def biegNastepny(self):
        if self.__bieg <= 6:
            self.__bieg += 1
            print(f"Bieg:{self.__bieg}")

    def biegPoprzedni(self):
        if self.__bieg >= 0:
            self.__bieg -= 1
            print(f"Bieg:{self.__bieg}")

    def przyspiesz(self):
        if self.__silnik is True and self.__bieg > 0:
            self.__predkosc += 10
            print(f"Prędkość:{self.__predkosc}")

    def hamuj(self):
        if self.__predkosc >= 10:
            self.__predkosc -= 10
            print(f"Prędkość:{self.__predkosc}")
        else:
            self.__predkosc = 0

car = Tesla()
car.uruchom()
car.biegNastepny()
car.przyspiesz()
# car.__predkosc = 300
car.przyspiesz()
car.hamuj()
car.hamuj()
car.biegPoprzedni()
car.wylacz()
