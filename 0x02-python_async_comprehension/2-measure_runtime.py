#!/usr/bin/env python3

"""
contains measure_runtime coroutine
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    executes async_comprehension four times
    in parallel using asyncio.gather
    """
    start_time = time.time()

    await asyncio.gather(*(async_comprehension() for i in range(4)))

    end_time = time.time()
    total_runtime = end_time - start_time

    return total_runtime
