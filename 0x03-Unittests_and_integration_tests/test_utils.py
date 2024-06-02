#!/usr/bin/env python3
"""A unitests module
"""
import unittest
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):
    """A unitests class 
    """
    @parameterized.expand([
        nested_map={"a": 1}, path=("a",)
        nested_map={"a": {"b": 2}}, path=("a",)
        nested_map={"a": {"b": 2}}, path=("a", "b")
    ])
    def test_access_nested_map(self, nested_map, path):
        self.assertEqual(TestAccessNestedMap(nested_map, path), path[-1])