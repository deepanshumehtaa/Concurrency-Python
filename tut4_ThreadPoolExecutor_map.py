"""
Thread Pool:
Reusing existing Threads, Because creating threads are expensive.
Also, Most of the computer OS caps the number of Thread that they can run.
And program could be crash if you will try to create more number of threads.

Why Creating Threads are Expensive ?
A: For that we need to look at the structure of Thread Pool:
    1.  components:
        1. Work Producers (tasks like Network call, i/o task, db connections, interrupts, rw to a file, etc)
        2. Job Queue (intermediate b/w producer and pool)
        3. Thread Pool (list of threads of fixed len)
    2. lot of calls to OS and OS need to allocate OS and CPU

So, ThreadPoolExecutor comes to rescue, an approach to keep up the throughput is to create & instantiate
a pool of idle threads beforehand and reuse the threads from this pool until all the threads are exhausted.
Also, the pool keeps track and manages the threads lifecycle and schedules them on the programmer’s behalf
thus making the code much simpler and less buggy.

we can use 3 methods to spawn threads from ThreadPoolExecutor:
1. map(fn, *iterables, timeout = None, chunksize = 1)
2. submit(fn, *args, **kwargs) -> Future:
3. shutdown(wait = True, *, cancel_futures = False)
    i. It must be called before executor.submit() and executor.map() method else it would throw RuntimeError.
    ii. It signals the executor to free up all resources when the futures are done executing.
    iii. wait=True makes the method not to return until execution of all threads is done and resources are freed up.
    iv. cancel_futures=True then the executor will cancel all the future threads that are yet to start.


`workers` are just MAX number of running tasks on parallel threads, hence a thread is nothing but worker !

"""

import time

import logging
import random

from threading import Thread, get_ident, current_thread
from threading import Timer  # utilized to run a code after a specified time period


# concurrent is the high level version of Threading to hide all the ugly working of thread details
from concurrent.futures import Future  # The upcoming proxy object
from concurrent.futures import ThreadPoolExecutor  # the Thread Pool Executor, Python 3.2+
# from concurrent.futures import ProcessPoolExecutor  # the Process Pool Executor
# from concurrent.futures import as_completed


# to see the concept of thread reusing we need to make uneven time period for each tasks
wait_time = 10


def some_func(item):
    # no_tasks = random.randrange(start=0, stop=10, step=1)
    logging.info(f"Task: {item} started!")
    # id of current Thread, is created by OS and id belongs to the worker
    logging.info(f'Thread {item}: id = {get_ident()}')
    logging.info(f'Thread {item}: name = {current_thread().name}')
    logging.info(f'Thread {item}: sleeping for {wait_time}')
    time.sleep(random.randrange(wait_time))
    logging.info(f'Thread {item}: finished')


# Main function
def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('App Start')

    cores = 4
    workers = 2*cores + 1
    items = 20

    # No need to Join the Threads
    # No need to Monitor or Handle the Threads
    # automatically spawn a new worker when there is
    # Said objects use significant amount of memory and for last project uses the large memory.
    # To reduce this memory management overhead (allocating and deallocating many threads)
    with ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(some_func, [1000, 1001, 1003, 1004])

    # some of the ids will gets repeated in the terminal that depicts the reuse of Threads
    logging.info('<<< App Finished >>>')


if __name__ == "__main__":
    main()

"""
INFO - 10:41:11: App Start
INFO - 10:41:11: Task: 1000 started!
INFO - 10:41:11: Thread 1000: id = 140681690216000
INFO - 10:41:11: Thread 1000: name = ThreadPoolExecutor-0_0
INFO - 10:41:11: Thread 1000: sleeping for 10
INFO - 10:41:11: Task: 1001 started!
INFO - 10:41:11: Thread 1001: id = 140681681823296
INFO - 10:41:11: Thread 1001: name = ThreadPoolExecutor-0_1
INFO - 10:41:11: Thread 1001: sleeping for 10
INFO - 10:41:11: Task: 1003 started!
INFO - 10:41:11: Thread 1003: id = 140681673430592
INFO - 10:41:11: Task: 1004 started!
INFO - 10:41:11: Thread 1003: name = ThreadPoolExecutor-0_2
INFO - 10:41:11: Thread 1004: id = 140681665037888
INFO - 10:41:11: Thread 1003: sleeping for 10
INFO - 10:41:11: Thread 1004: name = ThreadPoolExecutor-0_3
INFO - 10:41:11: Thread 1004: sleeping for 10
INFO - 10:41:14: Thread 1003: finished
INFO - 10:41:14: Thread 1001: finished
INFO - 10:41:16: Thread 1000: finished
INFO - 10:41:19: Thread 1004: finished
INFO - 10:41:19: <<< App Finished >>>
"""
