#!/usr/bin/env python3
"""
This module contains a function `measure_time` that calculates the
average runtime of running `wait_n` concurrently with multiple coroutines.
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average runtime of executing wait_n(n, max_delay).

    Args:
        n (int): Number of wait_random coroutines to spawn.
        max_delay (int): Maximum delay for each wait_random coroutine.

    Returns:
        float: Average time (in seconds) taken per coroutine.
    """
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.time()

    total_time: float = end - start
    return total_time / n
