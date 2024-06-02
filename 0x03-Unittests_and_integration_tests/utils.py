#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
import requests
from functools import wraps
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)

__all__ = [
    "access_nested_map",
    "get_json",
    "memoize",
]


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """Access nested map with key path.
    Parameters
    ----------
    nested_map: Mapping
        A nested map
    path: Sequence
        a sequence of key representing a path to the value
    Example
    -------
    >>> nested_map = {"a": {"b": {"c": 1}}}
    >>> access_nested_map(nested_map, ["a", "b", "c"])
    1
    """
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]

    return nested_map


def get_json(url: str) -> Dict:
    """Get JSON from remote URL.
    """
    response = requests.get(url)
    return response.json()


def memoize(fn: Callable) -> Callable:
    """Decorator to memoize a method.
    Example
    -------
    class MyClass:
        @memoize
        def a_method(self):
            print("a_method called")
            return 42
    >>> my_object = MyClass()
    >>> my_object.a_method
    a_method called
    42
    >>> my_object.a_method
    42
    """
    attr_name = "_{}".format(fn.__name__)

    @wraps(fn)
    def memoized(self):
        """"memoized wraps"""
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return property(memoized)


nested_map = {"a": {"b": {"c": 1}}, "d": 2, "e": [1, 2, {"f": 3}]}

# Accessing value at path "a", "b", "c"
value_1 = access_nested_map(nested_map, ["a", "b", "c"])
print(value_1)  # Output: 1

# Accessing value at path "d" (directly in the top level)
value_2 = access_nested_map(nested_map, ["d"])
print(value_2)  # Output: 2

# Trying an invalid path (key "x" doesn't exist)
try:
    value_3 = access_nested_map(nested_map, ["x", "y", "z"])
except KeyError as e:
    print(f"Error: {e}")  # Output: Error: 'x'

# Accessing a value within a list (path "e", index 2, key "f")
value_4 = access_nested_map(nested_map, ["e", 2, "f"])
print(value_4)  # Output: 3
