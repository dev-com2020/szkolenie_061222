# liczby = 4, 77, 123, 4323
# krotka = ('Tomek', "Kasia", "Aga", "Karol")
# ciekawostka = 5,
#
# print(liczby)
# print(sum(liczby))
# # print(sum(krotka))  # nie da się!
# print(ciekawostka)
# print(f"liczba {liczby[2]} jest na indeksie: {liczby.index(123)}")
# print(liczby[1:3])
#
lata = 22, 33, 44, 55
#
l1, *l2, l3 = lata
# print(l1)
# print(l2)
# print(l3)
# print(len(liczby))

lista = [43, 556]
cyfry = [43, 22, 543, 1, 423]
print(cyfry)
# cyfry.sort()
cyfry.reverse()
cyfry.append(l1)
cyfry.insert(2, l2)
cyfry.pop()
cyfry.remove(1)
cyfry.extend(lista)
cyfry[2] = 987
print(cyfry)
# lista2 = cyfry
lista2 = cyfry.copy()
print(lista2)
cyfry.append(l3)
print(lista2)