"""
Programme to run a big function task using MultiThreading
"""

import time

import logging
import random

from threading import Thread
from threading import Timer  # utilized to run a code after a specified time period

# from concurrent.futures import Future, ThreadPoolExecutor, ProcessPoolExecutor
# from concurrent.futures import as_completed
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Future

from queue import Queue

no_tasks = 7  #


def sub_task(name, x):
    logging.info(f'Starting Task {name}: {x}')
    time.sleep(2)
    logging.info(f'Finishing Task {name}: {x}')


sub_task_threads = []


def long_task(name):
    """This Function will take 14 sec to complete"""
    # no_tasks = random.randrange(start=0, stop=10, step=1)
    logging.info(f"Task: {name} performing {no_tasks} tasks with each 2 sec.")
    for x in range(no_tasks):
        t = Thread(target=sub_task, args=['thread: ' + str(x), x])
        sub_task_threads.append(t)
        t.start()

    logging.info(f'<<<< {name}: completed >>>>')


# Driver code .......................................
logging.info('Starting')
long_task("Main")

for t in sub_task_threads:
    t.join()


logging.info(f'At the End of the File')
