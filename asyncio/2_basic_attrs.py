import asyncio


async def c():
    return 1


async def main():
    task = asyncio.create_task(c())
    await task
    print(task.done())

asyncio.run(main())
