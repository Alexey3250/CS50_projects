# Trying out multithredding
import os
import time

from multiprocessing import Process, current_process

def square(numbers):
    """The function squares whatever is passed in"""
    for number in numbers:
        print(f"{current_process().name} squared {number} = {number * number}")
        time.sleep(0.5)
        
    # We can use the "os" module in Python to get the current process ID
    # assigned to the call of this function assigned by the OS.
    #process_id = os.getpid()
    #print(f"Process ID: {process_id}")

    # We can use the "multiprocessing" module in Python to get the current process ID
    process_name = current_process().name
    print(f"Process Name: {process_name}")


    return number * number

if __name__ == '__main__':
    processes = []
    numbers = range(100)

    for i in range(50):
        process = Process(target=square, args=(numbers,))
        processes.append(process)

        # Procecess are spawned by creating a Process object and then calling its start() method.
        process.start()

    for process in processes:
        process.join()
        print(f"{process.name} has finished")

    print("Multiprocessing complete.")