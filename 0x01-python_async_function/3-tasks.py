#!/usr/bin/env python3
""" Module that contains task_wait_random function. """

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Functino that creates an asyncio Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: The asyncio Task created for the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
