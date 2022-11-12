import time 
import concurrent.futures


def do_something(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return "Finished thread " 



with concurrent.futures.ThreadPoolExecutor() as executor:
    threads = [executor.submit(do_something, 2) for _ in range(10)]

    for thread in threads:
        print(thread.result())

