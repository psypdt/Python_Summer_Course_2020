from threading import Thread, Lock

mutex = Lock() # Create a lock which will be used to restrict access
final_result = 0 # Global variable which will store the final answer


# Iterative way of calculating the sum without threads
def calculate_sum(array):
    result = 0
    for element in array:
        result += element

    return result


def calculate_sum_thread(array):
    global final_result # We will write our answer to the global variable so we can access it from the main later on
    local_result = 0

    for i in range(0, len(array)):
        local_result += array[i]

    # Do all the mutexing outside the loop, prevents us from doing unneeded locks and unlocks
    mutex.acquire()
    final_result += local_result
    mutex.release()


if __name__ == '__main__':
    a = range(1000000)

    partition1 = a[0:int(len(a)/2)] # First half of the array
    partition2 = a[int(len(a)/2):len(a)] # Second half of the array
    partitions = [partition1, partition2] # The two array partitions get stored so we can assign them to the appropriate threads
    threads = list() # Keep track of the threads that we create

    for index in range(2):
        partition = partitions[index]
        x = Thread(target=calculate_sum_thread, args=[partition])
        threads.append(x) # Add the thread to the list of threads, so we can call join on it later on
        x.start() # Start running the thread


    # Wait for all the threads to finish before continuing
    for index, thread in enumerate(threads):
        thread.join()
        print(f'Thread {index} has finished')

    print(final_result)