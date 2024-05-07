#!/usr/bin/env python3
"""
A module that execute multiple
coroutines at the same time with async
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    A function that execute multiple coroutines
    at the same time with async
    """
    tasks = []
    delays = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for delay in asyncio.as_completed(tasks):
        delays.append(await delay)

    return delays
