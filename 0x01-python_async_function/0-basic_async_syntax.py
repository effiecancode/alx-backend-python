#!/usr/bin/env python3
"""async basic syntax program"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """An async function to return a random delay float

    Args:
        max_dalay (int): A max delay number parameter

    Returns:
        float: a random delay number

    """
    rand_num = random.random() * max_delay
    await asyncio.sleep(rand_num)
    return rand_num
