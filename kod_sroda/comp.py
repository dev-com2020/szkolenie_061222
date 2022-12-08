x = [i for i in range(5)]
# for i in range(5):
#     x.append(i)
print(x)

y = [i for i in range(10) if i % 2 == 0]
print(y)

lista = [1, 3, 4, 5, 7, 8]
lista = ['Parzysta' if i % 2 == 0 else 'Nieparzysta' for i in lista]
print(lista)
print(sum([i for i in range(10)]))
print(sum(i for i in range(10)))
