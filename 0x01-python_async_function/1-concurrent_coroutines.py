#!/usr/bin/env python3
""" Module that contains wait_n asynchronous coroutine. """

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ 
    Asynchronous coroutine that spawns wait_random n times 
    and returns a list of delays in ascending order.
    
    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random call.
        
    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = []
    tasks = []
    for i in range(n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
