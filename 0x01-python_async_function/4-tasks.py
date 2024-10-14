#!/usr/bin/env python3
""" Module that contains task_wait_n function. """

from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function that creates multiple asyncio Tasks
    for wait_random and returns a list of delays.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay for each wait_random call.

    Returns:
        List[float]: A list of delays in the order they completed.
    """
    futures = [task_wait_random(max_delay) for _ in range(n)]
    futures = asyncio.as_completed(futures)
    delays = [await future for future in futures]
    return delays
