from fastapi import APIRouter, Depends, Form
from starlette.requests import Request
from sqlalchemy.orm import Session

from src.app.cart import services
from src.utils.depencies import get_db

router = APIRouter()


@router.get('')
def cart_detail(request: Request, db: Session = Depends(get_db)):
    return services.cart_detail(request, db)


@router.post('/add')
def cart_add(
        request: Request,
        db: Session = Depends(get_db),
        id: int = Form(...),
        quantity: int = Form(...),
        update: bool = Form(...)):
    return services.cart_add(request, db, id, quantity, update)


@router.get('/remove_all')
def cart_remove(request: Request, db: Session = Depends(get_db)):
    return services.cart_remove_all(request, db)


@router.get('/remove/{id}')
def cart_remove(request: Request, id: int, db: Session = Depends(get_db)):
    return services.cart_remove(request, id, db)
