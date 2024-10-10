#!/usr/bin/env python3
""" Module that contains the safely_get_value function. """

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')  # Declare a type variable


def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
    """Function that safely retrieves a value from a dictionary."""
    if key in dct:
        return dct[key]
    else:
        return default
