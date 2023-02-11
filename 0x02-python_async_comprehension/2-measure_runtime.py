#!/usr/bin/env python3
"""Async funtion"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """return the time to execute the function async_comprehension 4 time"""
    prev = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return (time.perf_counter() - prev)
