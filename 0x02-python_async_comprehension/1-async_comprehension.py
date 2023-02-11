#!/usr/bin/env python3
"""Async function"""

import asyncio
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> list[float]:
    """Call the async_generator and return the output"""
    return [i async for i in async_generator()]
