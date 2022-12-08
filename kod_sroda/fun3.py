def many(imie="nieznany", *args, **kwargs):
    print(imie)
    print(args)
    print(kwargs)

jezyk = "polski"

many()
many("Tomek")
many("Ania", 34, 54, 66, 333, jezyk=jezyk)
many("Ania", 34, 54, 66, 333, wiek=19)
