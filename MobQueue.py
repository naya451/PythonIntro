import asyncio
import collections

async def sender(queue, pattern):
    for string in pattern:
        await queue.put(string)
    await queue.put(None)

async def reader(queue, number):
    counter = collections.Counter()
    i = 0
    while i < number:
        string = await queue.get()
        if string is None:
            i += 1
            continue
        counter[string] += 1
    return counter
