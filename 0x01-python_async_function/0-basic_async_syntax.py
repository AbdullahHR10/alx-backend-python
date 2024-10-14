#!/usr/bin/env python3
""" Module that contains wait_random asynchronous coroutine. """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Asynchronous coroutine that generates a random float
    between 0 and max_delay (inclusive), then waits for that delay.

    Args:
        max_delay (int): The maximum delay value (default is 10).

    Returns:
        float: The random delay that was waited for.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
