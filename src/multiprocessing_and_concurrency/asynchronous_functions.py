import asyncio
import time


async def one():
    print("One started")
    await asyncio.sleep(1)
    print("One ended")


async def two():
    print("Two started")
    await asyncio.sleep(4)
    print("Two ended")


async def three():
    print("Three started")
    await asyncio.sleep(2)
    print("Three ended")


async def main():
    # asyncio.create_task(one())
    # asyncio.create_task(two())
    # await asyncio.create_task(three())
    tasks = (one, two, three)
    await asyncio.gather(*[asyncio.create_task(task()) for task in tasks])


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print(f"Time for all functions is {time.time() - start_time}")
