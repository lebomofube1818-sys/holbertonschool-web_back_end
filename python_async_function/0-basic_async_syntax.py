#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for a random
delay and returns the delay time.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously wait for a random float delay between 0 and max_delay.

    Args:
        max_delay (int): Maximum number of seconds to wait (inclusive).
                         Default is 10.

    Returns:
        float: The actual number of seconds waited.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
