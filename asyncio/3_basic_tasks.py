import asyncio


async def one():
    return 1


async def greet(timeout):
    await asyncio.sleep(timeout)
    return 'F*** the World'


async def main():
    result_1 = asyncio.create_task(one())
    result_2 = asyncio.create_task(greet(2))
    result_3 = asyncio.create_task(greet(3))
    result_4 = asyncio.create_task(greet(4))
    result_5 = asyncio.create_task(greet(2))
    result_6 = asyncio.create_task(greet(3))

    print(await result_1)
    print(await result_2)
    print(await result_3)
    print(await result_4)
    print(await result_5)
    print(await result_6)

asyncio.run(main())
