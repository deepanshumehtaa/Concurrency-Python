"""
Queue is use to pass messages back and Forth
"""

import time
import threading
from queue import Queue
from threading import Thread, Timer
import logging

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
logging.info('Starting')


def my_queue():
    Queue()


def my_timer(name, queue):
    t = ""

