from time import sleep, perf_counter
from threading import Thread

def task():
    print("Startuje z zadaniem...")
    sleep(1)
    print("Wykonane")


start_time = perf_counter()
task()
task()
end_time = perf_counter()

print(f"To zajęło {end_time - start_time: 0.2f} sek")
