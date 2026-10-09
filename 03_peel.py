import asyncio

from kitchenkit import *
from kitchenkit.prep import async_cook, async_microwave, peel_and_slice

async def lunch_prep():
    put_on_apron()
    avocado = peel_and_slice(Avocado())
    (meatloaf, pasta) = await asyncio.gather(
        async_microwave(Meatloaf()),
        async_cook(Pasta()),
    )
    serve_food(meatloaf, pasta)

if __name__ == "__main__":
    asyncio.run(lunch_prep())
