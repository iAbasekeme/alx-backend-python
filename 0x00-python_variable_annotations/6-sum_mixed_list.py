#!/usr/bin/env python3
"""
6. Complex types - mixed list
"""
from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
  rt: float = 0.0
  for i in mxd_lst:
    rt += i
  return rt
