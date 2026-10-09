import asyncio

from kitchenkit import *
from kitchenkit.prep import async_cook, async_microwave, peel_and_slice

async def lunch_prep():
    put_on_apron()
    (pasta, meatloaf, avocado) = await asyncio.gather(
        async_microwave(Meatloaf()),
        asyncio.to_thread(peel_and_slice, Avocado()),
        async_cook(Pasta()),
    )
    serve_food(avocado, meatloaf, pasta)

if __name__ == "__main__":
    asyncio.run(lunch_prep())
