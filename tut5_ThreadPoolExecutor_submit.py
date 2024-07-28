import time

import logging
import random

from threading import Thread, get_ident, current_thread
from threading import Timer  # utilized to run a code after a specified time period


# concurrent is the high level version of Threading to hide all the ugly working of thread details
from concurrent.futures import Future  # The upcoming proxy object
from concurrent.futures import ThreadPoolExecutor, Future  # the Thread Pool Executor, Python 3.2+
from typing import List

# from concurrent.futures import ProcessPoolExecutor  # the Process Pool Executor
# from concurrent.futures import as_completed

WAIT_TIME = 10


def some_func(item, other_item=None):
    logging.info(f"Task: {item} - {other_item} started!")
    logging.info(f'Thread {item}: id = {get_ident()}')  # id of current Thread (worker)
    logging.info(f'Thread {item}: name = {current_thread().name}')
    logging.info(f'Thread {item}: sleeping for {WAIT_TIME}')
    time.sleep(WAIT_TIME)
    logging.info(f'Thread {item}: finished')


# Main function
def main() -> List[Future]:
    workers = 3  # 2*cores + 1

    # ** No need to Join the Threads
    # ** No need to Monitor or Handle the Threads
    # ** Reuse the threads so memory efficient (allocating and deallocating many threads)
    results: List[Future]
    with ThreadPoolExecutor(max_workers=workers) as executor:
        # `submit` is more advanced, as it supports kwargs
        futures = [executor.submit(some_func, item=i, other_item="NA") for i in range(10)]
        results: List[Future] = [future.result() for future in futures]

    return results


if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('App Start >>>')
    futs: List[Future] = main()

    logging.info(f'{futs[0].done()}')
    logging.info('App Finished >>>')
