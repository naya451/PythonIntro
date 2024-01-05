import asyncio

class FilterQueue(asyncio.Queue):
    def __init__(self, maxsize=0, *, loop=None):
        super().__init__(maxsize, loop=loop)
        self.window = None

    def __contains__(self, item):
        return any(filter(item) for filter in self._queue)

    def later(self):
        if self.empty():
            raise asyncio.QueueEmpty
        item = self.get_nowait()
        self.put_nowait(item)

    def get(self, filter=None):
        if filter is None or not self.__contains__(filter):
            return self.get_nowait()
        while True:
            item = self.get_nowait()
            if filter(item):
                self.put_nowait(item)
                return item


async def putter(n, queue):
    for i in range(n):
        await queue.put(i)

async def getter(n, queue, filter):
    for i in range(n):
        await asyncio.sleep(0.1)
        yield await queue.get(filter)

async def main():
    queue = FilterQueue(10)
    asyncio.create_task(putter(20, queue))
    async for res in getter(20, queue, lambda n: n % 2):
        print(res)

asyncio.run(main())