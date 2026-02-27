#!/usr/bin/env python3
"""
This module contains a function `task_wait_random` that creates an
asyncio.Task from the wait_random coroutine with a specified delay.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task wrapping wait_random(max_delay).

    Args:
        max_delay (int): Maximum number of seconds wait_random can delay.

    Returns:
        asyncio.Task: The created asyncio Task object.
    """
    return asyncio.create_task(wait_random(max_delay))
