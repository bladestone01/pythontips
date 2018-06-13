import uuid
import asyncio

import aiohttp
from get_photos import out_wrapper, user_conf, save_flag

async def download_one(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            save_flag(await resp.read(), str(uuid.uuid4()))

@out_wrapper
def download_many():
    urls = user_conf()
    loop = asyncio.get_event_loop()
    to_do = [download_one(url) for url in urls]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()
    return len(res)

if __name__ == '__main__':
    download_many()
