#!/usr/bin/env python3
"""A program to run async function"""
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes an async function n times

    Args:
        n (int): number of executions
        max_delay (int): The execution delay in seconds

    Returns:
        List[float]: A list of random numbers

    """
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(coroutines)]
