from time import sleep, perf_counter
import threading


start_time = perf_counter()

def dosomething(seconds):
    print(f"Ill sleep {seconds}... ")
    sleep(seconds)
    print("Wakeup")

threads = []

for _ in range(10):
    t = threading.Thread(target=dosomething, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish_time = perf_counter()

print(f"The code takes {finish_time - start_time} minutos to execute")


