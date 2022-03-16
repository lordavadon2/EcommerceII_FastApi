from fastapi import APIRouter

from src.app.shop.router import router as shop_router
from src.app.cart.router import router as cart_router
from src.app.orders.router import router as order_router
from src.app.payment.router import router as payment_router
from src.app.coupon.router import router as coupon_router

api_router = APIRouter()

api_router.include_router(shop_router, tags=['shop'], prefix="/product")
api_router.include_router(cart_router, tags=['cart'], prefix="/cart")
api_router.include_router(order_router, tags=['order'], prefix="/order")
api_router.include_router(payment_router, tags=['payment'], prefix="/payment")
api_router.include_router(coupon_router, tags=['coupon'], prefix="/coupon")
