"""
`Async` Runs in the same thread, but it gives you the illusion of multithreading.
Async were using `Coroutine`

Coroutine Vs Thread:
    Now you might be thinking how coroutine is different from threads, both seem to do the same job.
    In the case of threads, it’s OS that switches b/w threads according to the scheduler.
    While in the case of a coroutine, it’s the programmer and programming language which decides when to switch coroutines.
    Coroutines work cooperatively multitask by 'suspending and resuming' at set points by the programmer.

For DRF: https://nchan.io/

coroutine:
    A running asynchronous function. So if you define a function as `async def f()` and call it as `f()`
    you get back a coroutine. 
    python, async ==> coroutine
    Similarly, in JS, async ==> 
    
    So, coroutine is concurrency design pattern, that you can use to simplify code that executes asynchronously.

awaitable:
    anything that works with await like:
        coroutines, asyncio.Futures, asyncio.Tasks, objects that have a __await__ method.

Note: every AsyncIO program has at least one event loop.
"""

import time
import random
import logging
# import threading
import asyncio
import aiohttp

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
logging.info('Starting ...')


def display():
    ...


async def work1():
    logging.info("Work1 has been started")
    # doing some work
    await asyncio.sleep(2)  # calling a coroutine
    logging.info("Work1 has been ended")


async def work2():
    logging.info("Work2 has been started")
    # doing some work
    await asyncio.sleep(2)   # calling a coroutine
    logging.info("Work2 has been ended")


async def run_async():
    """controller for other async functions"""
    task_list = []  # has type of '_asyncio.Task'
    for x in range(10):
        name = "task:" + str(x)
        # wrapping the coroutines and converting it to Future
        # we are saving in list, bcoz it creates strong reference
        # A task that isn’t referenced elsewhere may get garbage-collected at any time, even before it’s done.
        task_list.append(asyncio.ensure_future((work1())))

    logging.info(f"Tasks list: {[i.get_name() for i in task_list]} {task_list[2].get_loop()}")


    await asyncio.gather(*task_list)  # wait for the other tasks to complete their future


def main():
    eloop = asyncio.get_event_loop()
    # eloop.run_forever()
    # eloop.run_in_executor()
    eloop.run_until_complete(future=run_async())

    eloop.close()  # free up resources & stops the loop for running infinitely [like a file]


main()


"""
Other Ex:

import asyncio

async def sample_coroutine():
    return 1212

async def main_coroutine():
    coroutine_object = sample_coroutine()
    # With await, we stop execution, give control back to the 
    # eventloop, and come back when the result of the 
    # coroutine_object is available.
    result = await coroutine_object
    assert result == 1212
# Blocking call to get the event loop, schedule a task, and close
# the event loop
asyncio.run(main_coroutine())
"""
