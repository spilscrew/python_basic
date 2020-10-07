import asyncio
import random


async def one(n):
    for num in range(n):
        await asyncio.sleep(random.randint(1, 15))
        print(num, 'one', n)
        await asyncio.sleep(random.randint(1, 15))


tasks = asyncio.wait([one(n) for n in range(1, 5)])
asyncio.run(tasks)
