import jinja2
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette_context.middleware import ContextMiddleware

from src.app.cart.cart import Cart
from src.utils.depencies import get_db


class CartMiddleware(ContextMiddleware):

    @jinja2.pass_context
    def cart(context: dict, db: Session = Depends(get_db)):
        request = context['request']
        return Cart(request, db)
