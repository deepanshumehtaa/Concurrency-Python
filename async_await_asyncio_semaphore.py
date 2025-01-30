import asyncio
import time
import threading

semaphore = asyncio.Semaphore(3)  # Allow up to 3 concurrent accesses


async def access_shared_resource(task_id):
    async with semaphore:
        print(f"Task {task_id} is accessing the shared resource")
        await asyncio.sleep(2)  # Simulate some work


async def main():
    tasks = []
    for i in range(10):
        task = asyncio.create_task(access_shared_resource(i))
        tasks.append(task)

    await asyncio.gather(*tasks)

start_time = time.time()
asyncio.run(main())
print(f"Total execution time: {time.time() - start_time} seconds")
