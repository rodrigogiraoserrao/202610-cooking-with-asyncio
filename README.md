# Cooking with `asyncio`

To run code:

 1. You can use `uv`:

`uv run --with kitchenkit lunch.py`

 2. You can install the dependency `kitchenkit` in a virtual environment and then run the code.

---

1. The smarter person managing me is the **event loop**.

2. Async code is still **single-threaded**.

3. The work to be done (tasks) need to be async-aware.