### Multithreading
#### when to use
##### I/O bound tasks:tasks that spend more time waiting for I/O operations (eg : file operation, network requests)
##### concurrent execution: when you want to improve throughput of your application by performing multiple operation conqurently

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)   #stops the code execution for number of seconds
        print(f"Number:{i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")

#creating threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)

start = time.time()
#start the threads
t1.start()
t2.start()

# wait for threads to complete
t1.join()
t2.join()

finished_time = time.time()-start
print(finished_time)



