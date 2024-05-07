#!/usr/bin/env python3
"""
A function that measures time
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    a function that measures total execution time
    """
    total_time = 0.0

    for _ in range(n):
        start_time = time.time()
        await wait_n(n, max_delay)  # Assuming wait_n is also an async function
        end_time = time.time()
        elapsed_time = end_time - start_time
        total_time += elapsed_time

    average_time = total_time / n
    return float(average_time)
