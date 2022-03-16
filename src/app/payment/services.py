from sqlalchemy.orm import Session
from starlette.requests import Request

from src.app.orders import crud
from src.app.payment.liqpay import LiqPay
from src.utils.config import LIQPAY_PUBLIC_KEY, LIQPAY_PRIVATE_KEY
from src.utils.depencies import templates, env


def checkout_payment(request: Request, order_id: int, db: Session):
    order_items = crud.get_order_items(db, order_id)
    total_price = sum(item.price for item in order_items)
    order_discount = crud.get_order_discount(db, order_id)
    if order_discount:
        total_price -= order_discount

    signature, data = payment_process(total_price, order_id)

    return templates.TemplateResponse(env.get_template('checkout.html'),
                                      {
                                          'request': request,
                                          'signature': signature,
                                          'data': data,
                                      })


def payment_process(total_price: float, order_id: int, ):
    liqpay = LiqPay(LIQPAY_PUBLIC_KEY, LIQPAY_PRIVATE_KEY)
    params = {
        'action': 'pay',
        'amount': f'{total_price}',
        'currency': 'USD',
        'description': f'Payment for order №{order_id}',
        'order_id': order_id,
        'version': '3',
    }
    signature = liqpay.cnb_signature(params)
    data = liqpay.cnb_data(params)

    return signature, data
