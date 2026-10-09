from kitchenkit import *
from kitchenkit.prep import async_cook, async_microwave

def lunch_prep():
    put_on_apron()
    meatloaf = await async_microwave(Meatloaf())
    pasta = async_cook(Pasta())
    serve_food(pasta, meatloaf)

if __name__ == "__main__":
    lunch_prep()