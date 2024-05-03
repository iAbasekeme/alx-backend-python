#!/usr/bin/env python3
"""
7. Complex types - string and int/float to tuple
"""
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
  """
  Creates a tuple containing a string key and the square of the provided value.
  """
  return k, v * v
