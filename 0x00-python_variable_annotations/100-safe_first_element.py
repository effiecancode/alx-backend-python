#!/usr/bin/env python3
"""
Duck Typing
"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Safely returns the first element of a sequence of None
    if the sequence is empty
    """
    if lst:
        return lst[0]
    else:
        return None
