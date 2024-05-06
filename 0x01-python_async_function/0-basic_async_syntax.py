#!/usr/bin/env python3
"""
A module tat implements coroutines
"""
__all__ = ['wait_random']
import random
import asyncio


async def wait_random(max_delay=10):
  ran = random.uniform(0, max_delay)
  await asyncio.sleep(ran)
  return ran
