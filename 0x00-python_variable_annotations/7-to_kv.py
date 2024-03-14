#!/usr/bin/env python3
"""
Type-annotation module
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    function to takes a str k and an int OR float v
    as arguments and returns a tuple
    """
    return k, float(v * v)
