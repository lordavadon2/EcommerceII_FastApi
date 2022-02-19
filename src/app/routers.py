from fastapi import APIRouter

from src.app.shop.router import router as shop_router
from src.app.cart.router import router as cart_router

api_router = APIRouter()

api_router.include_router(shop_router, tags=['shop'], prefix="/product")
api_router.include_router(cart_router, tags=['cart'], prefix="/cart")