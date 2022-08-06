# Youtube tutorial from Corey Schafer
# Python multiprocessing tutorial
import time
import multiprocessing

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} second...")
    time.sleep(seconds)
    print("Done sleeping...")

processes = []

# A list of processes
for _ in range(10):
    # Create a new process
    p = multiprocessing.Process(target=do_something, args=(1.5,))
    # Start the process
    p.start()
    # Add the process to the list
    processes.append(p)

for process in processes:
    process.join()

# Prints the time it took to complete
finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} second(s)")

# newer vesrision of python requires to use the tuple instead of a list
# for the args
