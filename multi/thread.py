# Multithreading
from threading import Thread
import os
import time
import math

def calc():
    for i in range(1, 1000000):
        math.sqrt(i)

threads = []

for i in range(os.cpu_count()):
    print(f"Creating thread {i}")
    threads.append(Thread(target=calc))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()