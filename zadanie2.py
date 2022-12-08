slownik = {"imie": "Zosia", "nazwisko": "Nowak", "wiek": 15, "jezyk": "Polski"}
# klucz = 1
for klucz in slownik:
    print(klucz, "=>", slownik[klucz])
if "wiek" in slownik:
    print("jest element o kluczu 'wiek'")
    del slownik['wiek']
slownik["PESEL"] = 12231354321
for k, v in slownik.items():
    print(k, "=>", v)
print(len(slownik))
