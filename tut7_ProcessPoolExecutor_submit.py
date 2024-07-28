"""
ThreadPoolExecutor vs ProcessPoolExecutor:
    most important difference is the type of workers used by each class.
    ProcessPoolExecutor runs each worker in its own separate child process.
    ThreadPoolExecutor runs each worker in separate threads within the main process.

    ref: https://www.geeksforgeeks.org/difference-between-process-and-thread/
    * Each separate child process has its own separate GIL.
    * But child processes don't share any variables.
    * The process is isolated, But Threads share memory & resources.
    * syscalls are involved in process, but not in Threads.

    But, Major use case is `ProcessPool` is for CPU bound tasks so, you can benefit from multiple CPU.


Q: Do time.sleep() suspend the execution of thread or process ?
A: Current Thread will get suspended.

Q: Any similarity b/w Thread and Process?
A: A thread is a path of execution within a process.

Q: what is Context Switching, only limited to MultiThreading?
A:  A context switch (also sometimes referred to as a process switch or a task switch)
    is the switching of the CPU (central processing unit) from one process or thread to another.
    This helps to share a single CPU across all processes to complete its execution and store the system's tasks status.

    But, the context switching for MultiProcessing is different from context switching in MultiThreading.
    ref: https://www.geeksforgeeks.org/difference-between-thread-context-switch-and-process-context-switch/

"""

# example of the map and wait pattern for the ProcessPoolExecutor
import logging
from time import sleep
import random
from concurrent.futures import ProcessPoolExecutor


# custom task that will sleep for a variable amount of time
def some_func(num):
    t = random.randrange(0, 5)
    sleep(t)
    return t*num


if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('Starting')

    # start the process pool
    with ProcessPoolExecutor(10) as executor:
        # The processing of Future objects in the order they are completed may be the most
        # common usage pattern of submit() function with the ProcessPoolExecutor.

        future = executor.submit(some_func, 2)  # <Future at 0x11b244e80 state=running>
        logging.info(f"status {future.running()}")  # True
        logging.info(future.cancelled())  # False
        logging.info(future.done())  # False
        logging.info(future.result())  # Blocking i.e. programme wait to complete this 

        futures = [executor.submit(some_func, 2) for _ in range(50)]  # storing the future in collection

        # # this will print the o/p of the function
        # for future_ in futures:
        #     # logging.info(f"{future_.result()}")
        #     ...

        logging.info(future.done())  # True
        logging.info("Programme ends Here !!!")
