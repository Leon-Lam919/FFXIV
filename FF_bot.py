import asyncio
import logging

import aiohttp
import pyxivapi
from pyxivapi.models import Filter, Sort

async def fetch_example_results():
    
