# image_processing_script.py

import asyncio
import logging
import httpx
import os
from aiohttp import ClientSession
from aiopg.sa import create_engine
from aioqueue import aioqueue
from sqlalchemy import create_engine as sa_create_engine, Column, String, MetaData, Table, Index
from sqlalchemy.ext.declarative import declarative_base
from aiometer import AIOCounter
from prometheus_async.aio import time
from typing import Tuple

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Replace the ellipsis with your specific configurations
CONFIG = {
    "db": {
        "host": "postgres",
        "port": 5432,
        "database": "image_processing_db",
        "user": "db_user",
        "password": "db_password",
    },
    "google_api_key": "",
    "image_resize_dimensions": (256, 256),
    "output_resized_images": "resized_images",
}

Base = declarative_base()

class Image(Base):
    __tablename__ = 'images'
    query = Column(String, primary_key=True)
    image_data = Column(String)

async def download_image(session, url):
    async with session.get(url) as response:
        response.raise_for_status()  
        return await response.read()

async def resize_and_save(image_data, output_path):

    # Replace the ellipsis with your specific implementation
    with open(output_path, 'wb') as f:
        f.write(image_data)

async def save_to_db(engine, query, output_path):

    async with engine.acquire() as conn:
        await conn.execute(Image.insert().values(query=query, image_data=output_path))

async def process_queue(queue, session, engine, counter):
    while True:
        query = input("Enter the search query: ")
        url = input("Enter the URL for the image: ")

        try:
            image_data = await download_image(session, url)
            output_path = f"{CONFIG['output_resized_images']}/{query}_{url.split('/')[-1]}"
            await resize_and_save(image_data, output_path)
            await save_to_db(engine, query, output_path)
            logger.info(f"Successfully processed {url}")
            counter.increment()
        except Exception as e:
            logger.error(f"Error processing {url}: {e}")
        finally:
            queue.task_done()

async def main():
    queue = aioqueue()

    async with ClientSession() as session, create_engine(**CONFIG['db']) as engine:
        Base.metadata.create_all(engine)

        Index('ix_images_query', Image.query).create(bind=engine)

        os.makedirs(CONFIG["output_resized_images"], exist_ok=True)

        await process_queue(queue, session, engine, AIOCounter())

if __name__ == "__main__":
    asyncio.run(main())
