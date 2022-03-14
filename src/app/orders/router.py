from fastapi import APIRouter, Request, Depends, Form
from sqlalchemy.orm import Session
from starlette.background import BackgroundTasks

from src.app.orders import services
from src.utils.depencies import get_db

router = APIRouter()


@router.get('/create_order')
def order_add(request: Request,
              db: Session = Depends(get_db)):
    return services.get_order_add(request=request,
                                  db=db)


@router.post('/create_order')
def order_add(request: Request,
              bg_task: BackgroundTasks,
              first_name: str = Form(...),
              last_name: str = Form(...),
              email: str = Form(...),
              address: str = Form(...),
              postal_code: int = Form(...),
              city: str = Form(...),
              db: Session = Depends(get_db)):
    return services.save_order_add(request=request,
                                   first_name=first_name,
                                   last_name=last_name,
                                   email=email,
                                   address=address,
                                   postal_code=postal_code,
                                   city=city,
                                   db=db,
                                   bg_task=bg_task)
