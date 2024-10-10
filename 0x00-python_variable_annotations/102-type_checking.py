#!/usr/bin/env python3
""" Module that contains zoom_array function. """

from typing import Union, Any, Mapping, Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Functino that returns a list with each element of lst
    repeated factor times. """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
