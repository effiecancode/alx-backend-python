#!/usr/bin/env python3
"""An Async Comprehensions program"""
from typing import List

async_gen = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Returns a list of random numbers"""
    return [num async for num in async_gen()]
