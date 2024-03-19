#!/usr/bin/env python3
'''Basic async module'''

from asyncio import Task
from typing import Any
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    '''this function will wait for a random time and return it'''
    return asyncio.create_task(wait_random(max_delay))
