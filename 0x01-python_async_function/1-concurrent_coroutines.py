#!/usr/bin/env python3
'''Basic async module'''


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''this function will wait for a random time and return it'''
    delays = []
    tasks = []

    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    for task in tasks:
        delay = await task
        delays.append(delay)
    return delays
