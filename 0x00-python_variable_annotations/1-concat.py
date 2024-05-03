#!/usr/bin/env python3
"""
1. Basic annotations - concat
"""


def concat(str1: str, str2: str) -> str:
    """
    concatenate two string
    """
    # concate: str = str1 + str2
    res: str = "".join([str1, str2])
    return res
