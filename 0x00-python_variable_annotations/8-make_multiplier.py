#!/usr/bin/env python3
"""
Type-annotation
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as arg and
    returns a function that multiples a float by
    multiplier
    """
    def multiplier_function(x: float) -> float:
        """
        Callable function
        """
        return x * multiplier
    return multiplier_function
