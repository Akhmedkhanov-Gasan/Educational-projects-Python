import asyncio


async def one():
    return 1


async def greet():
    await asyncio.sleep(2)
    return 'F*** the World'


async def main():
    result_1 = await one()
    result_2 = await greet()

    print(result_1)
    print(result_2)

asyncio.run(main())
