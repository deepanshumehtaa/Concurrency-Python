"""
Race Conditions:
    When one resource gets modified by the multiple threads at sametime.

DeadLock:
    when Multiple Threads waiting for same resource. As Neither of them get that resource.
    methods to prevent deadlock: https://www.geeksforgeeks.org/deadlock-prevention/


with CPython Supports multiple threads within the same interpreter. This is Because of GIL (NOT in the scope of discussion).
GIL doesn't just lock a variable or function; it locks the entire interpreter.
ref: https://wiki.python.org/moin/GlobalInterpreterLock

Thread Locking:
    https://docs.python.org/3/library/threading.html?highlight=lock#threading.Lock

"""

import time

import threading
import random
from concurrent.futures import ThreadPoolExecutor

import logging
logging.basicConfig(
        format='%(levelname)s - %(asctime)s: %(message)s',
        datefmt='%H:%M:%S',
        level=logging.DEBUG
)


# we will try to increment/access this variable using multiple Threads
# `counter_07` is just a fancy name nothing else
counter_07 = 0


def my_non_locked_func(count: int):
    """
    Broken due to Race Condition
    """
    global counter_07  # The Global Variable
    thread_id = threading.get_ident()
    logging.info(f'Starting Thread: {thread_id}')

    for _ in range(count):
        counter_07 += 1
        logging.info(f"{counter_07}")
        time.sleep(random.randrange(0, 5))
        logging.info(f"{thread_id}:: {counter_07} += {1}")


def my_locked_simplified(count: int):
    global counter_07  # The Global Variable
    thread_id = threading.get_ident()
    logging.info(f'Starting Thread: {thread_id}')

    for _ in range(count):
        # locking simplified
        lock = threading.Lock()
        with lock:
            logging.info("Locked")
            counter_07 += 1
            time.sleep(random.randrange(0, 5))

        logging.info(f"{thread_id}:: {counter_07} += {1}")


def my_locked_func(count: int):
    global counter_07  # The Global Variable
    thread_id = threading.get_ident()
    logging.info(f'Starting Thread: {thread_id}')

    for _ in range(count):
        # locking
        lock = threading.Lock()
        lock.acquire()
        # lock.acquire()  # un comment to see the DeadLock
        try:
            counter_07 += 1
        finally:
            lock.release()

        logging.info(f"{thread_id}:: {counter_07} += {1}")


def main():
    logging.info(msg='App Start')
    # test(10)  # running the logic 10 times, result 10

    # Multi Threading
    # `submit` executes the tasks using ProcessPoolExecutor and has more control over async tasks
    #  submit() will return Future, and we can query status of tasks like:
    #  f.running(), f.done() or f.cancelled().
    worker = 3
    with ThreadPoolExecutor(max_workers=worker) as ex:
        for x in range(0, 10):
            logging.info("Loop Started")
            # with Broken Function
            ex.submit(my_non_locked_func, x)

            # with Locked Function
            # ex.submit(my_locked_func, x)

            # with Simplified Locked Function
            # ex.submit(my_locked_simplified, x)


if __name__ == '__main__':
    main()
    print(counter_07)
