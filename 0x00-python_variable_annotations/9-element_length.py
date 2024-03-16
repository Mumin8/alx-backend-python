#!/usr/bin/env python3
'''this will annotate the function appropriately'''


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''annotating the function appropriately'''
    return [(i, len(i)) for i in lst]
