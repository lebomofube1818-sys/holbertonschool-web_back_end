#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine `wait_n` that runs
multiple `wait_random` coroutines concurrently and returns the list of
delays in ascending order.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run `wait_random` n times concurrently and return the list of delays.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum number of seconds each wait_random can delay.

    Returns:
        List[float]: Delays from all spawned wait_random coroutines in
                     ascending order as they complete.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results: List[float] = []

    for coro in asyncio.as_completed(tasks):
        result = await coro
        results.append(result)

    return results
