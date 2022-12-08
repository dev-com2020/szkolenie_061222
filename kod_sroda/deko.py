import time


def wykonaj(funkcja, a, b):
    x = funkcja(a, b)
    return x


def glowna():
    def wew(a, b):
        return a * b

    x = wew(2, 3)
    return x


def funk():
    def fWew(a, b):
        return a / b

    return fWew


x = funk()
print(x(30, 2))


def dodaj(a, b):
    return a + b


print(wykonaj(dodaj, 2, 3))
print(glowna())


def dekor(funkcja):
    def wew(*args, **kwargs):
        start = time.time()
        x = funkcja(*args, **kwargs)
        koniec = time.time()
        print(funkcja.__name__, "wykonywała się: ", koniec - start)
        return x

    return wew


@dekor
def zwykla(a, b, c):
    print("To jest zwykła funkcja")
    time.sleep(2)
    print(a + b + c)


@dekor
def odejmij(a, b):
    return a - b


zwykla(1, 2, 3)
odejmij(50, 4)
