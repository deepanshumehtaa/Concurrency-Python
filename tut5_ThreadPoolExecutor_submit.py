"""

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


def some_task(item):
    """This Function will take 14 sec to complete"""
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
    logging.basicConfig(
        format='%(levelname)s - %(asctime)s: %(message)s',
        datefmt='%H:%M:%S',
        level=logging.DEBUG
    )
    logging.info('App Start')

    cores = 4  # MacBook Pro cores (not including virtual cores)
    workers = 2*cores + 1
    items = 20

    # No need to Join the Threads
    # No need to Monitor or Handle the Threads
    # automatically spawn a new worker when there is
    # Said objects use significant amount of memory and for last project uses the large memory.
    # To reduce this memory management overhead (allocating and deallocating many threads)
    with ThreadPoolExecutor(max_workers=workers) as executor:
        # `max_workers`:  only use these number of workers
        executor.submit(some_task, range(0, items))

    # some of the ids will gets repeated in the terminal that depicts the reuse of Threads
    logging.info('App Finished')


if __name__ == "__main__":
    main()
