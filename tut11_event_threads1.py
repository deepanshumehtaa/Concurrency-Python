"""

"""
import logging
import threading
event = threading.Event()


logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
logging.info('Starting')


def my_some_function():
    logging.info(threading.current_thread().name)
    logging.info("Waiting for Event to happen ...")
    event.wait()  # stuck here until event is triggered
    logging.info("Performing some tasks XYZ now!")


t1 = threading.Thread(name="MyThread", target=my_some_function)
t1.start()


# from user input
x = input("\n Enter ur Input (just enter any damn thing)")
if x:
    event.set()  # triggering the event
else:
    pass


"""
Explanation:
    so there are two threads running `main` and `t1`, but the t1 was waiting for the event to happen
    and the main thread was waiting for the input.
"""
