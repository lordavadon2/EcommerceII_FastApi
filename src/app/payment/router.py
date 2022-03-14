from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.requests import Request

from src.app.payment import services
from src.utils.depencies import get_db

router = APIRouter()


@router.get('/checkout/{order_id}')
def checkout_payment(request: Request, order_id: int, db: Session = Depends(get_db)):
    return services.checkout_payment(request, order_id, db)
