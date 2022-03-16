from datetime import datetime

from sqlalchemy.orm import Session

from src.app.coupon import models


def get_coupon(db: Session, code: str, time_now: datetime):
    return db.query(models.Coupon).filter(models.Coupon.code == code,
                                          models.Coupon.valid_from.__le__(time_now),
                                          models.Coupon.valid_to.__ge__(time_now),
                                          models.Coupon.active == True).first()
