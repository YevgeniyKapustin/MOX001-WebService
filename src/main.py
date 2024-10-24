from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from loguru import logger
from redis import asyncio as aioredis
from starlette.middleware.cors import CORSMiddleware

from src.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url(
        'redis://localhost', encoding='utf8', decode_responses=True
    )
    FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')
    yield

app = FastAPI(
    title=settings.APP_TITLE,
    version='1.0',
    lifespan=lifespan,
    swagger_ui_parameters={
        'operationsSorter': 'method',
        'defaultModelsExpandDepth': -1
    },
)
# app.include_router(???)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.ORIGINS],
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'PATCH'],
    allow_headers=[
        'Access-Control-Allow-Headers', 'Access-Control-Allow-Origin',
        'Content-Type', 'Set-Cookie', 'Authorization'
    ],
)


logger.add('log.txt')


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
