# Newer easier way to do multi-threading
import time
import concurrent.futures

start = time.perf_counter()

# Define a function that takes a number of seconds to run
def do_something(seconds):
    print(f"Sleeping {seconds} second...")
    time.sleep(seconds)
    return 'Done sleeping...'

#
with concurrent.futures.ThreadPoolExecutor() as executor:
    # this method returns a future object
    seconds = [5, 4, 3, 2, 1]
    # Start the threads
    results = executor.map(do_something, seconds)
    # Get the results
    for result in results:
        print(result)

    # this method returns first results that are completed
    #results = [executor.submit(do_something, second) for second in seconds]
    #for f in concurrent.futures.as_completed(results):
        #print(f.result())

# Prints the time it took to complete
finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} second(s)")