from pathlib import Path

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from src.shop.router import router as shop_router

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

app.mount('/static', StaticFiles(directory=BASE_DIR / 'src/static'), name='static')

app.include_router(shop_router, tags=['shop'], prefix="/product")
