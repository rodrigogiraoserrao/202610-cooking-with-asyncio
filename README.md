# Cooking with `asyncio`

To run code:

 1. You can use `uv`:

`uv run --with kitchenkit lunch.py`

 2. You can install the dependency `kitchenkit` in a virtual environment and then run the code.

---

Create venv w/ uv:

```bash
% uv venv
% uv pip install kitchenkit
% uv run 04_to_thread.py
```

W/o uv:

```bash

```

---

1. The smarter person managing me is the **event loop**.

2. Async code is still **single-threaded**.

3. The work to be done (tasks) need to be async-aware.