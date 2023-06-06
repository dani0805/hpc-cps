import asyncio

async def main():
    future = asyncio.Future()

    # Schedule the set_result to be
    # called after two seconds
    asyncio.create_task(set_result(future))

    # This will pause the coroutine
    # until the future is resolved
    result = await future
    print(result)

async def set_result(future):
    await asyncio.sleep(2)
    future.set_result('Future is done!')

asyncio.run(main())