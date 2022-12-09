from time import sleep, perf_counter
from threading import Thread


def task(id):
    print(f"Startuje z zadaniem {id}")
    sleep(1)
    print(f"Wykonane zadanie {id}")


start_time = perf_counter()

threads = []

for n in range(1, 11):
    t = Thread(target=task, args=(n,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# t1 = Thread(target=task)
# t2 = Thread(target=task)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

end_time = perf_counter()

print(f"To zajęło {end_time - start_time: 0.2f} sek")
