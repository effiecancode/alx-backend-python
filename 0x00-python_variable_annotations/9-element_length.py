#!/usr/bin/env python3
"""
Type-annotation module
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    function that return a tuple which contain Sequence
    """
    return [(i, len(i)) for i in lst]
