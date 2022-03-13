from sqlalchemy.orm import Session

from src.app.orders import models


def create_order(db: Session,
                 first_name: str,
                 last_name: str,
                 email: str,
                 address: str,
                 postal_code: int,
                 city: str) -> models.Order:
    db_order = models.Order(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            address=address,
                            postal_code=postal_code,
                            city=city)
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
