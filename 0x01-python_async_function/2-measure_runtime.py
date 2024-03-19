#!/usr/bin/env python3
"""An program to measure the runtime of async function"""
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the async function execution time

    Args:
        n (int): The number of executions
        max_delay (int): The time delay in a function

    Returns:
        float: The total runtime elapsed in seconds

    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    runtime = (time.perf_counter() - start) / n
    return runtime
