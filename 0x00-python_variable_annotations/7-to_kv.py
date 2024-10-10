#!/usr/bin/env python3
""" Module that the to_kv function. """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Type-annotated function that takes a string and an int OR float
    as arguments and returns a tuple. """
    return (k, float(v ** 2))
