#!/usr/bin/env python3
'''this will floor a float'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Creates a tuple with a string key and the square of a numeric value.
    """
    return k, float(v ** 2)
