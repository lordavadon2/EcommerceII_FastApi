import datetime

from slugify import slugify
from sqlalchemy import Column, Integer, String, Text, DECIMAL, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType

from src.db.database import Base


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    slug = Column(String, unique=True)

    products = relationship('Product', back_populates='category')

    def __init__(self, *args, **kwargs):
        if 'slug' not in kwargs:
            kwargs['slug'] = slugify(kwargs.get('slug'))
        super().__init__(*args, **kwargs)


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    description = Column(Text)
    url = Column(URLType)
    price = Column(DECIMAL(scale=2))
    available = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.now)
    slug = Column(String, unique=True)

    def __init__(self, *args, **kwargs):
        if 'slug'not in kwargs:
            kwargs['slug'] = slugify(kwargs.get('slug'))
        super().__init__(*args, **kwargs)

    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', back_populates='products')
    order_item = relationship('OrderItem', back_populates='product_order')
