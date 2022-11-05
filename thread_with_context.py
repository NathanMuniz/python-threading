import concurrent.futures
import time
from unittest import result 

def so_something(seconds):
	print(f'Sleeping {seconds} second(s)...')
	time.sleep(seconds)
	
	return f'Done Sleeping...{seconds} seconds...'

with concurrent.futures.ThreadPoolExecutor() as executer:
	result = [executer.submit(so_something, 2) for _ in range(10)]

	for f in concurrent.futures.as_completed(result):
		print(f.result())	