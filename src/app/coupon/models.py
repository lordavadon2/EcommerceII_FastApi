import datetime

from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType

from src.db.database import Base


class Coupon(Base):
    __tablename__ = 'coupons'

    id = Column(Integer, autoincrement=True, primary_key=True)
    code = Column(String(50), unique=True)
    valid_from = Column(DateTime)
    valid_to = Column(DateTime)
    discount = Column(Integer)
    active = Column(Boolean)

    order = relationship('Order', back_populates='coupon')
