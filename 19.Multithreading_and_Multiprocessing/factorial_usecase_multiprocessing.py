'''
Real-World Example: Multiprocessing for CPU-bound tasks
Scenario: Factorial calculation
factorial calculation, especially for large numbers,
involves significant computational work. Multiprocessing
can be used to distribute the workload across mutliple cpu cores, improved performance.

'''

import multiprocessing
import math
import sys
import time

sys.set_int_max_str_digits(100000)   # function is used to configure the maximum number of digits allowed in the string representation of an integer in Python. Here's why this function might be used:

## function to compute factorial of a given number

def compute_factorial(number):
    print(f"Computing Factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == "__main__":
    numbers = [5000, 6000, 4000, 700]
    start = time.time()

    # create a pool of worker process
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)

    end = start - time.time()

    print(f"Results: {results}")
    print(f"Time Taken: {end} seconds")


'''
multiprocessing.Pool creates a pool of worker processes, each running in its own Python
interpreter. This allows multiple processes to execute simultaneously, taking advantage 
of multiple CPU cores.

'''



