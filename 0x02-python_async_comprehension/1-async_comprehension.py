#!/usr/bin/env python3
'''coroutine to collect 10 random numbers'''

import asyncio
from typing import List
from random import uniform

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    the function that coroutine will collect random numbers
    '''
    return [i async for i in async_generator()]
