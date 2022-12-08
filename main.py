from pakiet.obiekt import Human
from pakiet.obiekt2 import Human2

cz3 = Human2("Maciej", 22, "m")
cz3.przywitaj()
cz3.licz(6, 4)
cz3.ruszaj()

cz1 = Human()
cz1.imie = "Adam"
cz1.wiek = 23
cz1.plec = 'm'

cz1.przywitaj()
cz1.ruszaj()
cz1.licz(5, 5)

cz2 = Human()
cz2.imie = "Ewa"
cz2.wiek = 3
cz2.plec = 'kobieta'

cz2.przywitaj()
cz2.ruszaj()
cz2.licz(5, 5)

lista = [cz1, cz2]
print(lista)
