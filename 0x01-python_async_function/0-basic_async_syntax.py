'''python async function'''
#!/usr/bin/env python3
import random
import asyncio
'''async function wait_random that takes in an integer max_delay and returns a random float value with the specified max_delay'''


async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
