### Multithreading with thread Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number: {number}"

numbers = list(range(1, 6))

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number, numbers)
    
for result in results:
    print(result)