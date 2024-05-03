#!/usr/bin/env python3
"""
8. Complex types - functions
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a float by a given value.
    """
    def multiply(num: float) -> float:
        return num * multiplier
    return multiply
