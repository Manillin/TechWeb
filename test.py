import asyncio
import time


async def wait_me(time, i):
    await asyncio.sleep(time)
    print(f"Caller {i} finished waiting!")


async def main():
    l = []
    l.append(wait_me(10, 1))
    l.append(wait_me(5, 2))
    l.append(wait_me(1, 3))

    await asyncio.gather(*l)

    print("\n --- ")

asyncio.run(main())
