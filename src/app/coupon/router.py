from fastapi import APIRouter, Request, Depends, Form
from sqlalchemy.orm import Session

from src.app.coupon import services
from src.utils.depencies import get_db

router = APIRouter()


@router.get('/create_order')
def order_add(request: Request,
              db: Session = Depends(get_db)):
    return services.get_order_add(request=request,
                                  db=db)


@router.post('/apply')
def coupon_apply(request: Request,
                 code: str = Form(...),
                 db: Session = Depends(get_db)):
    return services.coupon_apply(request=request, code=code, db=db)
