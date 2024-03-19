#!/usr/bin/env python3
"""An async function to execute multiple coroutines asynchronously"""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """an async function to return a list of delay times

    Args:
        n (int): number of function execution
        max_dalay (int): max delay time

    Returns:
        List[float]: a list of random delay numbers

    """
    # Create list of courites objects execute n times
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    # use asyncio.as_completed() function to process results in real time
    return [await task for task in asyncio.as_completed(tasks)]
