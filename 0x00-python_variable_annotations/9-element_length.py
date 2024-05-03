#!/usr/bin/env python3
"""
9. Let's duck type an iterable object
"""

from typing import Iterable, Tuple, List


def element_length(lst: Iterable) -> List[Tuple[str, int]]:
  """
  Returns a list of tuples containing the element and its length for each element in an iterable.
  """
  return [(i, len(i)) for i in lst]
