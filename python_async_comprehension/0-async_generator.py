#!/usr/bin/env python3
"""0. Async Generator"""

import asyncio
import random


async def async_generator():
    """
    Coroutine that yields 10 random numbers between 0 and 10.
    Waits 1 second between each yield.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10

