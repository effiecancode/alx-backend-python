#!/usr/bin/env python3
"""
Measure runtijme
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the time it takes to run wait_n
    return the total average time taken per coroutine
    """
    start_time = time.time()
    # Records the current time  b4 calling the wait_n function
    asyncio.run(wait_n(n, max_delay))
    # asyncio.run function to run the wait_n function
    # calculates the total time takens to execute the wait_n fun
    stop_time = time.time()
    # Records the current time after the wait_n function has completed
    total_time = stop_time - start_time
    return total_time / n
