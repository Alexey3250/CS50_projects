# POOL

import time
from multiprocessing import Pool

def sum_square(number):
    s = 0
    for i in range(number):
        s += i * i
    return s

def sum_square_pool_with_mp(numbers):
    start_time = time.time()
    p = Pool()
    result = p.map(sum_square, numbers)


    p.close()
    p.join()

    print(f"Time taken: {time.time() - start_time} using multiprocessing")

def sum square no mp(numbers):
    start_time = time.time()
    result = []
    for number in numbers:
        result.append(sum_square(number))
    print(f"Time taken: {time.time() - start_time} using serial processing")

if __name__ == '__main__':

    numbers = range(100)
    sum_square_pool_with_mp(numbers)
    sum_square_no_mp(numbers)
    print("Multiprocessing complete.")


    #numbers = range(100)
    #start = time.time()
    #with Pool(processes=4) as pool:
    #    results = pool.map(lambda x: x * x, numbers)
    #end = time.time()
    #print(f"Time taken: {end - start}")
    #print(results)
    #print(f"Multiprocessing complete.")