from time import sleep, perf_counter
from threading import Thread

def task():
    print("Startuje z zadaniem...")
    sleep(1)
    print("Wykonane")


start_time = perf_counter()

t1 = Thread(target=task)
t2 = Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()

end_time = perf_counter()


print(f"To zajęło {end_time - start_time: 0.2f} sek")
