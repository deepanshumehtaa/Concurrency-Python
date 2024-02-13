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
    logger.info(f'Starting Task {name}: {x}')
    time.sleep(2)
    logger.info(f'Finishing Task {name}: {x}')


def long_task(name):
    """This Function will take 14 sec to complete"""
    # no_tasks = random.randrange(start=0, stop=10, step=1)
    no_tasks = 10
    logger.info(f"Task: {name} performing {no_tasks} tasks with each 2 sec.")
    sub_task_threads = []
    for x in range(no_tasks):
        t = Thread(target=sub_task, args=['thread: ' + str(x), x])
        sub_task_threads.append(t)
        t.start()

    logger.info(f'<<<< {name}: completed >>>>')
    return sub_task_threads


# Driver code .......................................
logger.info('Starting')
sub_task_threads = long_task("Main")

tt = sub_task_threads[0]
print(tt.is_alive(), tt.name, tt.isAlive())

for t in sub_task_threads:
    t.join()


logger.info(f'At the End of the File')
