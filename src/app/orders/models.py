import datetime

from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType

from src.db.database import Base


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, autoincrement=True, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(EmailType)
    address = Column(String)
    postal_code = Column(String)
    city = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    is_paid = Column(Boolean, default=False)

    order_item = relationship('OrderItem', back_populates='order')

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(Base):
    __tablename__ = 'order_item'

    id = Column(Integer, autoincrement=True, primary_key=True)
    price = Column(DECIMAL(scale=2))
    description = Column(Text)
    quantity = Column(Integer, default=1)

    product_id = Column(Integer, ForeignKey('product.id'))
    product_order = relationship('Product', back_populates='order_item')

    order_id = Column(Integer, ForeignKey('orders.id'))
    order = relationship('Order', back_populates='order_item')

    def get_cost(self):
        return self.price * self.quantity
