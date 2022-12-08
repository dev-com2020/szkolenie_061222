import random


def dodawanie(a, b=0):
    wynik = a + b
    return wynik


def test():
    x = []
    for i in range(random.randint(1, 10)):
        x.append(i)
    return tuple(x)

wynik = dodawanie(5, 5)
x = random.randint(1, 10)
print(x)
y = random.randint(1, 10)
print(y)

lista = [dodawanie(1), dodawanie(x, y), dodawanie(b=3, a=2), wynik]
print(lista)
test_lista = test()
print(test_lista)

