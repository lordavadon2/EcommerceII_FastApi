from sqlalchemy.orm import Session

from src.app.shop import models


def product_list(category_slug: str, db: Session):
    if category_slug:
        category = db.query(models.Category).filter_by(slug=category_slug).first()
        return db.query(models.Product).filter_by(category=category).all()

    return db.query(models.Product).all()


def category_list(db: Session):
    return db.query(models.Category).all()


def get_category_by_slug(category_slug: str, db: Session):
    return db.query(models.Category).filter_by(slug=category_slug).first()


def product_detail(db: Session, id: int, slug: str):
    return db.query(models.Product).filter_by(id=id, slug=slug).first()


def get_product_by_product_id(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()
