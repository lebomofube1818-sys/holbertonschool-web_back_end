#!/usr/bin/env python3
"""This module provides a function that returns a list of tuples with
elements of an iterable and their lengths.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples where each tuple contains an element and
    its length.
    """
    return [(i, len(i)) for i in lst]
