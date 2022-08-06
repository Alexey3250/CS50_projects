import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} second...")
    time.sleep(seconds)
    return f'Done sleeping...{seconds}'

with concurrent.futures.ProcessPoolExecutor() as executor:
    seconds = [4, 3, 2, 1]
    results = executor.map(do_something, seconds)

# Prints the time it took to complete
finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} second(s)")