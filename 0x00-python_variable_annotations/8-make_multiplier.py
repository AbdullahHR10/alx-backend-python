#!/usr/bin/env python3
""" Module that contains the make_multiplier function. """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Type-annotated function that takes a float multiplier and returns
    a function that multiplies a float by multiplier."""

    def multiply(value: float) -> float:
        return multiplier * value

    return multiply
