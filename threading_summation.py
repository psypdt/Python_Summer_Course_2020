from threading_mutex import Thread, Lock


mutex = Lock()
final_result = 0


def calculate_sum_thread(array):
    global final_result

    for i in range(0, len(array)):
        mutex.acquire()
        final_result += array[i]
        mutex.release()

if __name__ == '__main__':
    a = range(1000000)

    partition1 = a[0:int(len(a)/2)]
    partition2 = a[int(len(a)/2):len(a)]
    partitions = [partition1, partition2]
    threads = list()

    for index in range(2):
        partition = partitions[index]
        x = Thread(target=calculate_sum_thread, args=[partition])
        threads.append(x)
        x.start()


    for index, thread in enumerate(threads):
        thread.join()
        print(f'Thread {index} has finished')

    print(final_result)
