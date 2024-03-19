#!/usr/bin/env python3
"""An Async Generator Program"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """An async generator that yields a random number ten times"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
