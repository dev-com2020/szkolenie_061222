a = 5
b = 10

def mnozenie():
    global a
    a = 100
    wynik = a * b
    return wynik

print(mnozenie())
print(f"Wartość zmiennej a: {a}")