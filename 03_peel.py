import asyncio

from kitchenkit import *
from kitchenkit.prep import async_cook, async_microwave, peel_and_slice

async def async_peel_and_slice(food):
    return peel_and_slice(food)

async def lunch_prep():
    put_on_apron()
    (avocado, meatloaf, pasta) = await asyncio.gather(
        async_peel_and_slice(Avocado()),
        async_microwave(Meatloaf()),
        async_cook(Pasta()),
    )
    serve_food(avocado, meatloaf, pasta)

if __name__ == "__main__":
    asyncio.run(lunch_prep())
