import asyncio


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
    print("main thread")
    await task2
    print("main thread")
    await task3
    print("main_driver ended ...")


asyncio.run(main_driver())

"""
o/p:


main_driver started ...
xx started
yy started
xx says ohhhoo....
yy says ohhhoo....
['ok xx', 'ok yy']
main_driver ended ...
"""
