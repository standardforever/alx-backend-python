#!/usr/bin/env python3
"""Asyncronous function"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Using yeild for a random number and wait for 1sec"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
