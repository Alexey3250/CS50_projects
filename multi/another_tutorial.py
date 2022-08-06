# youtube: corey schafer
# Python threading tutorial
import time
import threading

start = time.perf_counter()

# Define a function that takes a number of seconds to run
def do_something(seconds):
    print(f"Sleeping {seconds} second...")
    time.sleep(seconds)
    print("Done sleeping...")

# A list of threads
threads = []

# Create 10 threads
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Prints the time it took to complete
finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} second(s)")
