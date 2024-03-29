import asyncio

"""
More advanced than `asyncio.gather(*coroutines)`,
because `asyncio.gather(*coroutines)` perfect in scheduling and de-scheduling with corouting & during this they
don't interfear with the main thread !

BUT, `create_task` kind of spawn a thead for each task and can ALSO context switch with the main thread asyncly.
"""

async def xx():
    print("xx started")
    await asyncio.sleep(4)  # Yield control back to the event loop (not necessary in this case)
    print("xx says ohhhoo....")
    return "ok xx"


async def yy():
    print("yy started")
    await asyncio.sleep(2)  # Yield control back to the event loop (not necessary in this case)
    print("yy says ohhhoo....")
    return "ok yy"


async def zz():
    print("zz started")
    await asyncio.sleep(1)  # Yield control back to the event loop (not necessary in this case)
    print("zz says ohhhoo....")
    return "ok zz"


# (BEST method) calling through via some `main_driver`:
async def main_driver_v1():
    task1 = asyncio.create_task(xx())
    task2 = asyncio.create_task(yy())
    task3 = asyncio.create_task(zz())

    print("main_driver started ...")
    await task1
    print("main thread1")
    await task2
    print("main thread2")
    await task3
    print("main_driver ended ...")



####################################################################

async def main_driver_v2():
    """No Guratee paralalis v1 is better"""
    tasks = [xx(), yy(), zz()]  # List of coroutines to execute
    
    print("main_driver started ...")
    for task in tasks:
        await asyncio.create_task(task)  # Create a task for each coroutine

asyncio.run(main_driver_v2())

"""
o/p:
main_driver started ...
xx started
yy started
zz started
zz says ohhhoo....
yy says ohhhoo....
xx says ohhhoo....
main thread1
main thread2
main_driver ended ...
"""
