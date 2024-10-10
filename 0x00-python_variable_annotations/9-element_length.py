#!/usr/bin/env python3
""" Module that contains the function element_length. """

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that takes an iterable of sequences and returns
    a list of tuples containing each sequence and its length."""
    return [(i, len(i)) for i in lst]
