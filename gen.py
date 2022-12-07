def fibo():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


fib = fibo()

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

for i in fibo():
    print(i)
    if i > 10:
        break


print(next(fib))
print(next(fib))