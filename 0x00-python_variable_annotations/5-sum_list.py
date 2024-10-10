#!/usr/bin/env python3
""" Module that contains the function sum_list. """


def sum_list(input_list: list[float]) -> float:
    """ Type-annotated function that takes a list of floats
    and returns their sum as a float."""
    sum: float = 0.0
    for number in input_list:
        sum += number
    return sum
