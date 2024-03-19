#!/usr/bin/env python3
"""A program that uses asyncio to create tasks"""
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """A function that create an async task

    Args:
        max_delay (int): Execution delay in seconds

    Returns:
        asnycio.Task: an async task

    """
    return asyncio.create_task(wait_random(max_delay))
