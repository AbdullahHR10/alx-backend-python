#!/usr/bin/env python3
""" Module that contains the sum_mixed_list function. """

from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """Type-annotated function that takes a list of integers and floats
    and returns their sum as a float."""
    return sum(input_list)
