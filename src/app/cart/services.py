from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette import status
from starlette.requests import Request
from starlette.responses import RedirectResponse

from src.utils.depencies import templates, env
from .cart import Cart
from ..shop import models
from ..shop.recommender import Recommender


def cart_detail(request: Request, db: Session):
    cart = Cart(request, db)

    recommender = Recommender()
    cart_products = list(jsonable_encoder([item['product'] for item in cart]))
    if cart_products:
        recommended_products = recommender.suggest_products_for(db, cart_products, max_result=4)
    else:
        recommended_products = None

    return templates.TemplateResponse(env.get_template('cart.html'),
                                      {
                                          'request': request,
                                          'cart': cart,
                                          'recommended_products': recommended_products,
                                      })


def cart_add(request: Request, db: Session, id: int, quantity: int, update: bool):
    cart = Cart(request, db)
    product = db.query(models.Product).filter_by(id=id).first()
    cart.add(product, quantity, update_quantity=update)

    return RedirectResponse(url='/cart', status_code=status.HTTP_303_SEE_OTHER)


def cart_remove(request: Request, id: int, db: Session):
    cart = Cart(request, db)
    product = db.query(models.Product).filter_by(id=id).first()
    cart.remove(product)

    return RedirectResponse(url='/cart', status_code=status.HTTP_303_SEE_OTHER)


def cart_remove_all(request: Request, db: Session):
    cart = Cart(request, db)
    cart.remove_all()

    return RedirectResponse(url='/cart', status_code=status.HTTP_303_SEE_OTHER)
