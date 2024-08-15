### MultiProcessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_numbers(numbers):
    time.sleep(1)
    return f"Square: {numbers * numbers}"

numbers = [1, 2, 3, 4, 5]

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=2) as executor:
        results = executor.map(square_numbers, numbers)

    for result in results:
        print(result)