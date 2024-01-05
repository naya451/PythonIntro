import asyncio

async def serial(number, barrier):
    await barrier.wait()
    print(f"Serial number: {number}")
    
from random import shuffle

async def main(num):
    bar = asyncio.Barrier(num)
    tasks = [serial(i * 2 % num, bar) for i in range(num)]
    shuffle(tasks)
    await asyncio.gather(*tasks)

asyncio.run(main(10)) 