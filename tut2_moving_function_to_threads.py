"""
Move a functions to multiple thread and will wait for all of them to complete
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


def long_task(name):
    """This Function will take 14 sec to complete"""
    # no_tasks = random.randrange(start=0, stop=10, step=1)
    logging.info(f"Task: {name} performing {no_tasks} tasks with each 2 sec.")
    for x in range(no_tasks):
        logging.info(f'Task {name}: {x}')
        time.sleep(2)
    logging.info(f'Task: {name}: completed')


# Main function

def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('Starting')

    # 1.
    # Synchronously running the function with taking 2 seconds of pause
    # long_task('main')

    # 2.
    # MultiThreading, calling long_task 7 times and everytime on a new thread.
    # hence taking overall 14 seconds 7*2 to complete all 7 function calls.
    threads: list[Thread] = []
    for x in range(no_tasks):
        t = Thread(target=long_task, args=['thread: ' + str(x)])
        threads.append(t)
        t.start()

    # The Blocking Point, Wait for all the threads to finish.
    # once finished and join then after that the code below gets executed.

    # also, my main thread is blocked
    # Q:    What if one of the child thread fail to gets execute and find itself in
    #       some infinitely waiting situation.
    for t in threads:
        t.join()

    # 3.
    # creating a thread for every single tasks
    # see tut3_threading_to_big_function.py

    logging.info('Finished all threads')


if __name__ == "__main__":
    main()
