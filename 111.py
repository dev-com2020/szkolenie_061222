# Lista1 = [1, 2, 3, 4]
# Lista2 = [2, 3, 4, 5]
# lista = Lista1 + Lista2

# for i in range(len(Lista1)):
#     print("wynik mnozenia:", (lambda x, y: x * y)(Lista1[i], Lista2[i]))

#
# print(f"Mapowanie: {list(map(lambda x,y: x * y, Lista1, Lista2))}")

Lista1 = [1, 2, 3, 4]
Lista2 = [2, 3, 4, 5]
def listownik(lista1, lista2):
    print(f"Wynik mnożenia list: {list(map(lambda x, y: x * y, lista1, lista2))}")
    return

listownik(Lista1, Lista2)
