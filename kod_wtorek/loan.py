# MIN_SALARY = 30000.0  # Wysokość minimalnego rocznego wynagrodzenia.
# MIN_YEARS = 2  # Minimalna liczba lat pracy u aktualnego pracodawcy.
#
# salary = float(input('Podaj wysokość rocznego wynagrodzenia: '))
#
# years_on_job = int(input('Podaj liczbę lat pracy u obecnego pracodawcy: '))
#
# if salary >= MIN_SALARY:
#     if years_on_job >= MIN_YEARS:
#         print("Masz zdolność kredytową!")
#     else:
#         print("Musisz być zatrudniony przez minimum", MIN_YEARS)
# else:
#     print("Musisz zarabiać przynajmniej", format(MIN_SALARY, '.2f'))
#
# MIN_SALARY = 30000.0  # Wysokość minimalnego rocznego wynagrodzenia.
# MIN_YEARS = 2  # Minimalna liczba lat pracy u aktualnego pracodawcy.
#
# salary = float(input('Podaj wysokość rocznego wynagrodzenia: '))
#
# years_on_job = int(input('Podaj liczbę lat pracy u obecnego pracodawcy: '))
#
# if salary >= MIN_SALARY and years_on_job >= MIN_YEARS:
#     print("Masz zdolność kredytową!")
# else:
#     print("Nie masz zdolności kredytowej")



# x = int(input("Podaj x"))
# if x >= 20 and x <= 40:
#     print("Mamy przedział!")

comm = 'Hello World3'
match comm:
    case 'Hello World':
        print('PASUJE!')
    case 'Bye World':
        print('NIE PASUJE!')
    case _:
        print('NIE ZNALEZIONO!')




# x = 3
# y = 1
# a = 6
# b = 9
# z = 1
#
# print(x > y and a < b)
# print(x == y or y == z)
# print(not (x > y))
