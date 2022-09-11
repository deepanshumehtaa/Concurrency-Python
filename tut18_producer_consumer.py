"""
TODO: need more clarity
producer will produce some work and consumer will do that work.
The producer is on other thread and consumer is on the other.
"""
import threading
import random
import logging
import multiprocessing as mp
# from asyncio import Queue  # this is new
from queue import Queue

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
logging.info('Starting ...')


def display(msg):
    thread_name = threading.current_thread().name
    process_name = mp.current_process().name
    logging.info(f'{process_name} - {thread_name}: {msg}')


# Producer
def create_work(queue, finished, max):
    finished.put(False)
    for x in range(max):
        v = random.randint(1, 100)
        queue.put(v)
        display(f'Producing {x}: {v}')
    finished.put(True)
    display('finished')


# Consumer
def perform_work(work, finished):
    counter = 0
    while True:
        if not work.empty():
            v = work.get()
            display(f'Consuming {counter}: {v}')
            counter += 1
        else:
            q = finished.get()
            if q is True:
                break
        display('finished')


# Main function
def main():
    max_ = 10
    work = Queue()
    finished = Queue()

    producer = threading.Thread(target=create_work, args=[work, finished, max_], daemon=True)
    consumer = threading.Thread(target=perform_work, args=[work, finished], daemon=True)

    producer.start()
    consumer.start()

    producer.join()
    display('Producer has finished')

    consumer.join()
    display('Consumer has finished')

    display('Finished')


if __name__ == "__main__":
    main()
