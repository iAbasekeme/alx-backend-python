#!/usr/bin/env python3
"""
5. Complex types - list of floats
"""


def sum_list(input_list: list[float]) -> float:
  """
  Calculates the sum of all elements in a list of floats.
  """
  rt: float = 0.0
  for i in input_list:
    rt += i
  return rt
