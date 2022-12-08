from enum import Enum, auto


class Weekday(Enum):
    PONIEDZIALEK = 0
    WTOREK = 1
    SRODA = 2
    CZWARTEK = 3
    PIATEK = 4
    SOBOTA = 5
    NIEDZIELA = 6

class OrderStatus(Enum):
    OCZEKIWANIE = auto()
    PRZETWARZANIE = auto()
    ZAKONCZONO = auto()

class Weekday2(Enum):
    PONIEDZIALEK = auto()
    WTOREK = auto()
    SRODA = auto()
    CZWARTEK = auto()
    PIATEK = auto()
    SOBOTA = auto()
    NIEDZIELA = auto()

print(OrderStatus.OCZEKIWANIE.name)
print(Weekday(1).value)
print(Weekday(3).name)
print(Weekday(6))

