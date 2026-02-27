#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine `task_wait_n` that
runs multiple `task_wait_random` tasks concurrently and returns
the list of delays in ascending order.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run `task_wait_random` n times concurrently and return the list
    of delays in ascending order as they complete.

    Args:
        n (int): Number of tasks to spawn.
        max_delay (int): Maximum delay each task can have.

    Returns:
        List[float]: Delays from all spawned tasks in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results: List[float] = []

    for coro in asyncio.as_completed(tasks):
        result = await coro
        results.append(result)

    return results
