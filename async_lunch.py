import asyncio

from kitchenkit import *
from kitchenkit.prep import async_cook, async_microwave

async def lunch_prep():
    put_on_apron()
    meatloaf = await async_microwave(Meatloaf())
    pasta = await async_cook(Pasta())

    asyncio.gather(
        async_microwave(Meatloaf()),
        async_cook(Pasta()),
    )

    serve_food(pasta, meatloaf)

if __name__ == "__main__":
    asyncio.run(lunch_prep())