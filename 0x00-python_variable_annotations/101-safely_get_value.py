#!/usr/bin/env python3
""" Module that contains the safely_get_value function. """

from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ Function that safely retrieves a value from a dictionary. """
    if key in dct:
        return dct[key]
    else:
        return default
