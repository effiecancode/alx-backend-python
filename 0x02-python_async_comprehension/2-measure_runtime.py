#!/usr/bin/env python3
"""A program to get runtime for parallel comprehension"""
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime of async functions"""
    start = time.perf_counter()
    coroutines = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*coroutines)
    runtime = time.perf_counter() - start

    return runtime
