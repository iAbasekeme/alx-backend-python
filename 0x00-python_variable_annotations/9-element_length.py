#!/usr/bin/env python3
"""
Let's duck type an iterable object
"""

from typing import Iterable, Tuple, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing the element and its length
    for each element in an iterable.
    """
    return [(i, len(i)) for i in lst]
