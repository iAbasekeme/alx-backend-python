#!/usr/bin/env python3
"""
A module that execute multiple
coroutines at the same time with async
"""
import random
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    A function that execute multiple coroutines
    at the same time with async
    """
    delays = [await wait_random(max_delay) for _ in range(n)]
    delays.sort()
    return delays
