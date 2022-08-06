# multiprocessing
from multiprocessing import Process
import os
import time
import math

def calc():
    for i in range(1, 1000000):
        math.sqrt(i)

processes = []

for i in range(os.cpu_count()):
    print(f"Creating process {i}")
    processes.append(Process(target=calc))

for process in processes:
    process.start()

for process in processes:
    process.join()