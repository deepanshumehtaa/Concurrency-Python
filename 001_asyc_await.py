import asyncio

async def xx():
    # we cant use await with `print` as it is not a goroutine
    # await print("xx")
    print("xx started")
    await asyncio.sleep(0)  # Yield control back to the event loop (not necessary in this case)
    print("ohhhoo....")
    await yy()
    return "ok xx"
    
async def yy():
    print("yy started")
    await asyncio.sleep(0)  # Yield control back to the event loop (not necessary in this case)
    return "ok yy"



# METHOD 1:
ans1 = asyncio.run(xx())  # run the event loop and execute the asynchronous code.
print(ans1)


# METHOD 2 (BEST method):
async def driver():
    coroutines = [xx(), yy()]
    results = await asyncio.gather(*coroutines)
    print(results)


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(driver())
