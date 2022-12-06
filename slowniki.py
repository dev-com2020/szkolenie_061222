slownik = {"gracz": {"imie": "Tomek", "wiek": 39},
           "punkty": [33, 44, 55, 66],
           "czy_pali": False}

slownik["przerwa"] = True
slownik["czy_pali"] = None

print(slownik)
print(slownik['gracz'])
print(slownik['gracz']['imie'])
print(slownik['punkty'][2])
print(slownik.values())
print(slownik.keys())
print(slownik.items())
print(slownik.get('gracz'))
del slownik['gracz']
print(slownik)




