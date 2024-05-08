#!/usr/bin/env python3
"""
A module that runs four parallel comprehensions
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    A function that measures the total runtime of all generators using
    asyncio.gather()
    """
    start_time = time.time()
    lists = await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = time.time()
    return end_time - start_time
