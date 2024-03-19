#!/usr/bin/env python3
"""
Asychronous coroutine that takes an integers args(max_delay)
with a default of 10 named wait random that waits for a random
delay btw 0 and max_delay(included and float vale) seconds and
eventually returns it
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    functions that return random float numbers
    """

    time_delayed = random.uniform(0, max_delay)
    await asyncio.sleep(time_delayed)
    return time_delayed
