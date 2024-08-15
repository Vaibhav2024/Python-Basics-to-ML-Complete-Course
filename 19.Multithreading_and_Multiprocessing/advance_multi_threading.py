### multithreading with thread pool executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number: {number}"

numbers = [1, 2, 3, 4, 5]

with ThreadPoolExecutor(max_workers=3) as executor:  # max_workers means max number of threads
    results = executor.map(print_number, numbers)

for result in results:
    print(result)





