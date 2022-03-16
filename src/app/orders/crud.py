from sqlalchemy.orm import Session

from src.app.orders import models


def create_order(db: Session,
                 first_name: str,
                 last_name: str,
                 email: str,
                 address: str,
                 postal_code: int,
                 city: str,
                 coupon_id: int = None,
                 discount: int = 0,
                 ) -> models.Order:
    db_order = models.Order(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            address=address,
                            postal_code=postal_code,
                            city=city,
                            coupon_id=coupon_id,
                            discount=discount
                            )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def create_order_item(db: Session,
                      item: dict,
                      order_id: int,
                      product_id: int) -> models.OrderItem:
    db_order_item = models.OrderItem(order_id=order_id,
                                     product_id=product_id,
                                     price=item['price'],
                                     quantity=item['quantity'])
    db.add(db_order_item)
    db.commit()
    db.refresh(db_order_item)
    return db_order_item


def update_order(db: Session, order_id: int):
    db_order = db.query(models.Order).filter_by(id=order_id).first()
    db_order.is_paid = True
    db.commit()
    # db.refresh(db_order)


def get_order_items(db: Session, order_id: int):
    return db.query(models.OrderItem).filter_by(order_id=order_id).all()


def get_order_discount(db: Session, order_id: int):
    return db.query(models.Order).filter_by(id=order_id).first().discount
