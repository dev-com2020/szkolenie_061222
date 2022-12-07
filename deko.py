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


def odejmij(a, b):
    return a - b


print(wykonaj(dodaj, 2, 3))
print(glowna())


def dekor(funkcja):
    def wew(*args, **kwargs):
        print("Dekorujemy funkcje")
        return funkcja(*args, **kwargs)

    return wew


@dekor
def zwykla(a, b, c):
    print("To jest zwykła funkcja")
    print(a + b + c)


zwykla(1,2,3)
