#!/usr/bin/env python3
'''this will return  product of two values'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''multiply and return product'''
    def multiplier_function(x: float) -> float:
        '''the multiplier function'''

        return x * multiplier
    return multiplier_function
