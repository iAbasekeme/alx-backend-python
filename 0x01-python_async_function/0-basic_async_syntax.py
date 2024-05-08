#!/usr/bin/env python30-async_generator.py
"""
A module tat implements coroutines
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    An asynchronous coroutine
    """
    ran = random.uniform(0, max_delay)
    await asyncio.sleep(ran)
    return ran
