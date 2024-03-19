#!/usr/bin/env python3
"""
Import wait_random from the prev python file  and write an async
routin called wait_n that takes 2 int args. You will spawn
wait_random n times with the specified max_delay
"""

import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    function that returns the list of all the delays
    (float values).The list shld be in ascending order
    """
    list_of_delays = []
    for w in range(n):
        delays = await wait_random(max_delay)
        list_of_delays.append(delays)
    return sorted(list_of_delays)
