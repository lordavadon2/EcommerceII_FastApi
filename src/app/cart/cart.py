from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette.requests import Request

from src.app.coupon import models
from src.utils.config import SECRET_KEY
from src.app.shop.models import Product


class Cart:
    def __init__(self, request: Request, db: Session) -> None:
        self._session = request.session
        self._db = db
        cart = self._session.get(SECRET_KEY)

        if not cart:
            cart = self._session[SECRET_KEY] = {}

        self._cart = cart
        self._coupon_id = self._session.get('coupon_id')

    @property
    def cart(self):
        return self._cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self._cart:
            self._cart[product_id] = {
                'quantity': 0,
                'price': str(product.price),
            }

        if update_quantity:
            self._cart[product_id]['quantity'] = quantity
        else:
            self._cart[product_id]['quantity'] += quantity

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self._cart:
            del self._cart[product_id]

    def remove_all(self):
        product_ids = list(self._cart.keys())

        for id in product_ids:
            del self._cart[str(id)]

    def __iter__(self):
        product_ids = list(self._cart.keys())
        products = self._db.query(Product).filter(Product.id.in_(product_ids)).all()
        cart = self._cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = jsonable_encoder(product)

        for item in cart.values():
            item['total_price'] = float(item['price']) * float(item['quantity'])

            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self._cart.values())

    def get_total_price(self):
        return sum(float(item['price']) * float(item['quantity']) for item in self._cart.values())

    @property
    def coupon(self):
        if self._coupon_id:
            return self._db.query(models.Coupon).filter(models.Coupon.id == self._coupon_id).first()
        return None

    def get_discount(self):
        if self.coupon:
            return float("{:.2f}".format((self.coupon.discount / float(100)) * self.get_total_price()))

        return float("{:.2f}".format(0))

    def get_total_price_after_discount(self):
        return float("{:.2f}".format(self.get_total_price()-self.get_discount()))

    @property
    def coupon_id(self):
        return self._coupon_id
