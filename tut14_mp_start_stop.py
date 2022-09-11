"""
TODO: This programme has error please rectify this

Starting and stopping the other process and getting their results.
"""

import time
import logging
# import threading
import multiprocessing as mp

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
logging.info('Starting ...')


def run(msg, num):
    name = mp.process.current_process().name
    ident = mp.process.current_process().ident
    logging.info(f"current process: {ident} {name}")

    for x in range(num):
        logging.info("")
        time.sleep(1)


worker = mp.Process(
    name="MyCustomProcess",
    target=run,
    args=("Working", 100),
    daemon=True,
)
worker.start()
time.sleep(5)

# terminating the ongoing process (not recommended, as this will force kill the process)
if worker.is_alive() is True:
    worker.terminate()

worker.join()
