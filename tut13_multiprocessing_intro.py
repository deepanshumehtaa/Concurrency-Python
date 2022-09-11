"""
- Every time you press the run button in Python, it starts a process to run that script.
- Every process has its own memory and threads.
- Multiple process can run same script across multiple processors
"""


import time
import logging
# import threading
import multiprocessing as mp

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
logging.info('Starting')


def run():
    name = mp.process.current_process().name
    daemon = mp.process.current_process().daemon
    ident = mp.process.current_process().ident
    logging.info(f"current process name: {name}")  # current process name: MainProcess
    logging.info(f"Extras: {daemon} {ident}")  # Extras: False 39917
    time.sleep(2)
    logging.info("returning run")


run()

# Multiprocessing
process_list = []
for x in range(5):
    pro = mp.Process(target=run, daemon=True)
    process_list.append(pro)
    pro.start()

# we will black the execution of MainProcess till all other process are done
for p in process_list:
    p.join()

logging.info("DONE!")
