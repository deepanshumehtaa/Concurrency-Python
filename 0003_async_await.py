import asyncio

"""
More advanced than `asyncio.gather(*coroutines)`,
because `asyncio.gather(*coroutines)` perfect in scheduling and de-scheduling with corouting & during this they
don't interfear with the main thread !

BUT, `create_task` kind of spawn a thead for each task and can ALSO context switch with the main thread asyncly.
"""

async def xx():
    print("xx started")
    await asyncio.sleep(1)  # Yield control back to the event loop (not necessary in this case)
    print("xx says ohhhoo....")
    return "ok xx"


async def yy():
    print("yy started")
    await asyncio.sleep(2)  # Yield control back to the event loop (not necessary in this case)
    print("yy says ohhhoo....")
    return "ok yy"


async def zz():
    print("zz started")
    await asyncio.sleep(4)  # Yield control back to the event loop (not necessary in this case)
    print("zz says ohhhoo....")
    return "ok zz"


# (BEST method) calling through via some `main_driver`:
async def main_driver():
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


asyncio.run(main_driver())

"""
o/p:


main_driver started ...
xx started
yy started
zz started
xx says ohhhoo....
main thread1
yy says ohhhoo....
main thread2
zz says ohhhoo....
main_driver ended ...
"""
