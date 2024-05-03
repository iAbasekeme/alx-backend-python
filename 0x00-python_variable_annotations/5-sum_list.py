#!/usr/bin/env python3
"""
5. Complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
  """
  Calculates the sum of all elements in a list of floats.
  """
  return float(sum(input_list))
