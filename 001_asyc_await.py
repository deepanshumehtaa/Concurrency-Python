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


# (BEST method) calling through via some `main_driver`:
async def main_driver():
    print("main_driver started ...")
    coroutines = [xx(), yy()]
    results = await asyncio.gather(*coroutines)
    print(results)
    print("main_driver ended ...")


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(main_driver())


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
