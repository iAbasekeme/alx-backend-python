#!/usr/bin/env python30-async_generator.py
"""
A module that implements async generators
"""
import random
import asyncio
from typing import List


async def async_generator() -> List[float]:
    """
    A function that generates asynchronously
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
