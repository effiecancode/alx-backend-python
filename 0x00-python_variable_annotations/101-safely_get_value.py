#!/usr/bin/env python3
"""
Duck Typing Module
"""
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely gets a value from a mapping
    (dictionary-like_object
    """
    if key in dct:
        return dct[key]
    else:
        return default
