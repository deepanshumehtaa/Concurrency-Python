import time
import threading
from threading import Thread, Timer
import logging

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
logging.info('Starting')


def my_timer():
    t = threading.get_ident()
    logging.info(f"starting: {t}")

    for i in range(60):
        logging.info(f"currently working by: {t}")
        time.sleep(1)

    logging.info(f"Time Up !")


def stop():
    logging.info("Exiting the Application")
    exit(0)  # will shut down everything


if __name__ == '__main__':
    logging.info("STARTING")

    # making a timer on new thread
    timer_ = threading.Timer(3, stop)
    timer_.start()

    # new thread
    t = threading.Thread(target=my_timer, daemon=False)  # now it is a daemon Thread
    t.start()


"""
So here a daemon thread will continue running even after the parent/main thread gets stop executing.

It doesn't mean that daemon thread will continue running forever, 
it will run until unless its work is done but totally independent of parent thread.
"""

