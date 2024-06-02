#!/usr/bin/env python3
"""A unitests module
"""
import unittest
from parameterized import parameterized

from utils import (
    access_nested_map,
    get_json,
    memoize,
)

class TestAccessNestedMap(unittest.TestCase):
    """A unitests class 
    """
    @parameterized.expand([
        ({"a": 1}, ("a",)),
        ({"a": {"b": 2}}, ("a",)),
        ({"a": {"b": 2}}, ("a", "b")),
    ])
    def test_access_nested_map(self, *args):
        """A method that performs unittest
        """
        nested_map, path = args
        self.assertEqual(test_access_nested_map(nested_map, path), nested_map[path[-1]])
