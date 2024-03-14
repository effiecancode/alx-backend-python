#!/usr/bin/env python3
"""
Duck Typing
"""
import typing


def zoom_array(lst: typing.Tuple, factor: int = 2) -> typing.List:
    """Variable annotation for list"""
    zoomed_in: typing.List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
