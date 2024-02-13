"""
Programme to run a big function task using MultiThreading
"""

import sys
import time

from threading import Thread
from threading import Timer  # utilized to run a code after a specified time period


import logging
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
logger.addHandler(logging.StreamHandler(stream=sys.stdout))


def sub_task(name, x):
    logging.info(f'Starting Task {name}: {x}')
    time.sleep(2)
    logging.info(f'Finishing Task {name}: {x}')


def long_task(name):
    """This Function will take 14 sec to complete"""
    # no_tasks = random.randrange(start=0, stop=10, step=1)
    no_tasks = 10
    logging.info(f"Task: {name} performing {no_tasks} tasks with each 2 sec.")
    sub_task_threads = []
    for x in range(no_tasks):
        t = Thread(target=sub_task, args=['thread: ' + str(x), x])
        sub_task_threads.append(t)
        t.start()

    logging.info(f'<<<< {name}: completed >>>>')
    return sub_task_threads


# Driver code .......................................
logging.info('Starting')
sub_task_threads = long_task("Main")

for t in sub_task_threads:
    t.join()


logging.info(f'At the End of the File')
