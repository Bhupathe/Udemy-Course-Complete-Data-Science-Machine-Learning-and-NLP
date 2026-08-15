## Processes that run in parallel
### CPU-Bound Tasks-Tasks that are heavy on CPU usage (e.g., mathematical computations, data processing).
## Parallel execution- Multiple cores of the CPU

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i**3}")
     
if __name__ == "__main__":   
## Create a 2 process
    t = time.time()   
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    ## Start the Process
    p1.start()
    p2.start()
    
    ## Wait for the process to complete
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print("%.11lf",finished_time)

 