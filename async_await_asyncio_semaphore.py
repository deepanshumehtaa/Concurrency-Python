import asyncio
import time
import threading

semaphore = asyncio.Semaphore(3)  # Allow up to 3 concurrent accesses


def some_blocking_fn():
    time.sleep(1)

global_dict = {}


async def access_shared_resource(task_id):
    async with semaphore:
        loop = asyncio.get_event_loop()
        await asyncio.sleep(2)  # Simulate some work

        with threading.Lock():
            global_dict[task_id] = task_id

        print(f"Task {task_id} is accessing the shared resource")

        # this is how we call blocking fn, in async way
        res = await loop.run_in_executor(
            executor=None,
            func=some_blocking_fn,
        )


async def main():
    tasks = []
    for i in range(10):
        task = asyncio.create_task(access_shared_resource(i))
        tasks.append(task)

    await asyncio.gather(*tasks)


start_time = time.time()
asyncio.run(main())
print(f"Total execution time: {time.time() - start_time} seconds")
print(global_dict)
