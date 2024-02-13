import asyncio

async def coroutine_one():
    print("Coroutine One is starting...")
    await asyncio.sleep(3)
    print("Coroutine One is done.")
    return "Result from Coroutine One"

async def coroutine_two():
    print("Coroutine Two is starting...")
    await asyncio.sleep(1)
    print("Coroutine Two is done.")
    return "Result from Coroutine Two"

async def main1():
    # Using asyncio.gather to run multiple coroutines concurrently
    results = await asyncio.gather(
        coroutine_one(),
        coroutine_two()
    )
    
    # Results will contain the return values of the coroutines
    print("Results:", results)

async def main2():
    results = await asyncio.gather(
        *[coroutine_one(), coroutine_two()]
    )
    
    # Results will contain the return values of the coroutines
    print("Results:", results)


# Run the event loop with the main coroutine
asyncio.run(main2())
