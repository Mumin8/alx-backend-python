#!/usr/bin/env python3
'''this will floor a float'''


from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """Sums a list of integers and floats.

    Args:
        mxd_lst: A list containing integers or floats.

    Returns:
        The sum of the integers and floats in the list as a float.
    """

    return sum(mxd_lst)
