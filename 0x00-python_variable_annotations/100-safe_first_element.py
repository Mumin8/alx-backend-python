#!/usr/bin/env python3
'''this will annotate a function appropriately'''


from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    '''it will annotate the function as expectedS'''
    if lst:
        return lst[0]
    else:
        return None
