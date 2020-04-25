from multiprocessing import Process
import os
import time



def info(title):
    print(title)
    print('module name:', __name__)
    print('Pid of the parent process:', os.getppid())
    print('Pid of the current process:', os.getpid())


# Example function1
def func1(name):
    time.sleep(4)
    info('Calling function: func1')
    print('hello', name)



# Example function2
# This function utilises the fork() method to spawn a child process
def func2():
    pid_flag = os.fork() # Returns 0 for child process and non-zero for parent process

    if pid_flag > 0:
      print('The parent process has a PID: ', os.getpid())

    else:
      print('The child process has a PID: ', os.getpid())





if __name__ == '__main__':
    func2()

    print('main entry point into program with pid:', os.getpid())
    p = Process(target=func1, args=('Joe',))
    p.start()
    p.join()

    print("Finished the main")







