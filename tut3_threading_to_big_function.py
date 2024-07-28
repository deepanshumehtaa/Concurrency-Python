"""
Programme to run a big function task using MultiThreading
"""

import sys
import time

from threading import Thread
from threading import Timer  # utilized to run a code after a specified time period


import logging
from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
logger.addHandler(logging.StreamHandler(stream=sys.stdout))


def sub_task(name, x):
    logger.info(f'Starting Task {name}: {x}')
    time.sleep(5)
    logger.info(f'Finishing Task {name}: {x}')


def long_task(no_tasks) -> List[Thread]:
    """This Function will take 14 sec to complete"""
    # no_tasks = random.randrange(start=0, stop=10, step=1)
    logger.info(f"long_task performing {no_tasks} tasks with each 5 sec.")
    sub_task_threads: List[Thread] = []
    for x in range(no_tasks):
        t = Thread(target=sub_task, args=['thread: ' + str(x), x])
        sub_task_threads.append(t)
        t.start()

    logger.info('<<<< returning long_task >>>>')
    return sub_task_threads


# Driver code .......................................
logger.info('Starting ...')

no_tasks = 10
sub_task_threads = long_task(no_tasks)
tt: Thread = sub_task_threads[0]

print(tt.is_alive(), tt.ident)

for t in sub_task_threads:
    t.join()

logger.info('Exit ...')
