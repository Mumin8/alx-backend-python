#!/usr/bin/env python3
'''Basic async module'''


import asyncio
from typing import Any
from asyncio import Task


def task_wait_random(max_delay: int) -> Task:
    '''this function will wait for a random time and return it'''
    return asyncio.create_task(wait_random(max_delay))
