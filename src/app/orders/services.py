from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status
from starlette.background import BackgroundTasks
from starlette.requests import Request
from starlette.responses import RedirectResponse

from src.app.cart.cart import Cart
from src.app.orders.mail import Mail
from src.app.shop.recommender import Recommender
from src.utils.depencies import templates, env
from src.app.orders import crud
from src.app.shop import crud as shop_crud


def get_order_add(request: Request, db: Session):
    cart = Cart(request, db)

    return templates.TemplateResponse(env.get_template('order.html'),
                                      {
                                          'request': request,
                                          'cart': cart,
                                      })


def save_order_add(request: Request,
                   first_name: str,
                   last_name: str,
                   email: str,
                   address: str,
                   postal_code: int,
                   city: str,
                   db: Session,
                   bg_task: BackgroundTasks):
    cart = Cart(request, db)

    recommender = Recommender()

    db_order = crud.create_order(db=db,
                                 first_name=first_name,
                                 last_name=last_name,
                                 email=email,
                                 address=address,
                                 postal_code=postal_code,
                                 city=city,
                                 coupon_id=cart.coupon_id,
                                 discount=cart.get_discount())
    order_id = db_order.id

    request.session['order_id'] = order_id

    recommending = []
    for item in cart:
        product_id = item['product']['id']
        crud.create_order_item(db=db,
                               order_id=order_id,
                               product_id=product_id,
                               item=item)
        recommending.append(shop_crud.get_product_by_product_id(db, product_id))

    cart.remove_all()

    mail = Mail()
    bg_task.add_task(mail.send_notification)

    recommender.products_bought(recommending)

    crud.update_order(db=db, order_id=order_id)

    return RedirectResponse(url=f'/payment/checkout/{order_id}', status_code=status.HTTP_303_SEE_OTHER)
