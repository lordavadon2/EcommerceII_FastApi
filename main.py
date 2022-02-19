from pathlib import Path

import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette_context.middleware import ContextMiddleware

from src.app import routers
from src.utils.config import SECRET_KEY
from src.utils.context_processors import CartMiddleware
from src.utils.depencies import env

BASE_DIR = Path(__file__).resolve().parent

middleware = [
    Middleware(SessionMiddleware, secret_key=SECRET_KEY),
    Middleware(CartMiddleware),
]

app = FastAPI(middleware=middleware)

env.globals["cart_context"] = CartMiddleware.cart

app.mount('/static', StaticFiles(directory=BASE_DIR / 'src/static'), name='static')

app.include_router(routers.api_router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
