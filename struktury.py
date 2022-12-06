liczby = 4, 77, 123, 4323
krotka = ('Tomek', "Kasia", "Aga", "Karol")
ciekawostka = 5,

print(liczby)
print(sum(liczby))
# print(sum(krotka))  # nie da się!
print(ciekawostka)
print(f"liczba {liczby[2]} jest na indeksie: {liczby.index(123)}")
print(liczby[1:3])

lata = 22, 33, 44, 55

l1, *l2, l3 = lata
print(l1)
print(l2)
print(l3)
