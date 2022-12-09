from time import perf_counter

def replace(filename, substr, new_substr):
    print(f'Procesuje plik {filename}')
    with open(filename, 'r') as f:
        content = f.read()

    content = content.replace(substr, new_substr)

    with open(filename, 'w') as f:
        f.write(content)

def main():
    filenames = [
        'example/test1.txt',
        'example/test2.txt',
        'example/test3.txt',
        'example/test4.txt',
        'example/test5.txt',
        'example/test6.txt',
        'example/test7.txt',
        'example/test8.txt',
        'example/test9.txt',
        'example/test0.txt',
    ]

    for filename in filenames:
        replace(filename, 'test', 'id')


start_time = perf_counter()
main()
end_time = perf_counter()
print(f"To zajęło {end_time - start_time: 0.2f} sek")



