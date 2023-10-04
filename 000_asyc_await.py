
"""
Noob async/await it is, it really not way you write async code,
because it will work same as that of sync code !!
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


async def driver():
    print("driver1... ")
    ans_xx = await xx()
    print("driver2... ", ans_xx)
    ans_yy = await yy()
    print("driver3... ", ans_yy)
    return "ok yy"

ans1 = asyncio.run(driver())  # run the event loop and execute the asynchronous code.
print(ans1)
