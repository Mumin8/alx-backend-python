#!/usr/bin/env python3
'''Basic async module'''


import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    '''this function will wait for a random time and return it'''

    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
