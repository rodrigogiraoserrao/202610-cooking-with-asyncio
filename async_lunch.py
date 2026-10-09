from kitchenkit import *
from kitchenkit.prep import async_cook, async_microwave

async def lunch_prep():
    put_on_apron()
    gathered_tasks = asyncio.gather(
        async_microwave(Meatloaf()),
        async_cook(Pasta()),
    )
    (pasta, meatloaf) = await gathered_tasks
    serve_food(pasta, meatloaf)
