from kitchenkit import *
from kitchenkit.prep import cook

import time

def microwave(food):
    time.sleep(3)
    return food

def lunch_prep():
    put_on_apron()
    meatloaf = microwave(Meatloaf())
    pasta = cook(Pasta())
    serve_food(pasta, meatloaf)

if __name__ == "__main__":
    lunch_prep()