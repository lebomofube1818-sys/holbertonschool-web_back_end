#!/usr/bin/env python3
"""This module provides a function that returns a tuple of a string and
the square of a number as a float.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple where the first element is the string and the second
    element is the square of the number as a float.
    """
    return (k, float(v ** 2))
