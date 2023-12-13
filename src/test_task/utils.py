import asyncio

lock = asyncio.Lock()


async def work() -> None:
    async with lock:
        await asyncio.sleep(3)
