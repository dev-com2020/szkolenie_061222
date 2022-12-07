lista = [4, 55, 65, 4, 77, 23]
zbior = set(lista)
zbior2 = {55, 4, 77, 123, 333, 456, 77}
print(zbior)
print(zbior2)
print(zbior.difference(zbior2))
print(zbior2.difference(zbior))
print(zbior.intersection(zbior2))
lista = list(zbior)
print(lista)