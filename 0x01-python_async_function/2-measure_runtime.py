#!/usr/bin/env python3
""" Module that contains wait_n asynchronous coroutine. """

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time of wait_n(n, max_delay)
    and returns the average time per call.

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay for each call.

    Returns:
        float: Average execution time per call to wait_n.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    return (end_time - start_time) / n
