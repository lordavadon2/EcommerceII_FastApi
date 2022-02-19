import datetime

from sqlalchemy import Column, Integer, String, Text, DECIMAL, Boolean, DateTime

from src.db.database import Base


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    description = Column(Text)
    price = Column(DECIMAL(scale=2))
    available = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.now)
