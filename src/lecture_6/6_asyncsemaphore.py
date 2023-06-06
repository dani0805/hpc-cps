import asyncio
import random

# Simulate a semaphore allowing only 3 concurrent connections
semaphore = asyncio.Semaphore(3)

async def fetch_data(worker_number):
    await semaphore.acquire()
    try:
        print(f"Worker {worker_number} has started fetching data.")
        # Simulate the time taken to fetch the data
        await asyncio.sleep(random.randint(2, 5))
        print(f"Worker {worker_number} has finished fetching data.")
    finally:
        semaphore.release()

async def main():
    # Creating a future for each worker
    workers = [fetch_data(i) for i in range(10)]
    # Using asyncio.gather to schedule the execution of all workers concurrently
    await asyncio.gather(*workers)

# Get the current event loop
loop = asyncio.get_event_loop()

# If the loop is not already running, we can use run_until_complete
if not loop.is_running():
    loop.run_until_complete(main())
# If the loop is already running, we can create a new task in the loop
else:
    loop.create_task(main())