## it allows us to run multiple process in parallel
## when to use
## CPU-Bound task(heavy on cpu usage task, mathematical computation)
## Parallel execution - multiple cores of cpu

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Square: {i * i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cubes: {i*i*i}")

if __name__ == "__main__":
    # create 2 processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    start = time.time()
    ## start the process 
    p1.start()
    p2.start()

    # wait for process to complete

    p1.join()
    p2.join()
    finished_time = time.time() - start
    print(finished_time)