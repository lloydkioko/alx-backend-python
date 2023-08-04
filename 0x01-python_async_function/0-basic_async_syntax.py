#!/usr/bin/env python3
"""
Asynchronous Python Module
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """takes an argument and waits for a random delay"""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
