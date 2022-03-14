from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session

from src.app.shop import services
from src.utils.depencies import get_db

router = APIRouter()


@router.get('')
def get_product_list(request: Request,
                             db: Session = Depends(get_db)):
    return services.get_all_data(request=request,
                                 db=db)


@router.get('/{category_slug}')
def get_product_list_by_slug(request: Request,
                             category_slug: str,
                             db: Session = Depends(get_db)):
    return services.get_all_data(request=request,
                                 category_slug=category_slug,
                                 db=db)


@router.get('/{product_id}/{product_slug}')
def get_product_detail(request: Request,
                       product_id: int,
                       product_slug: str,
                       db: Session = Depends(get_db)):
    return services.product_detail(request=request,
                                   product_id=product_id,
                                   product_slug=product_slug,
                                   db=db)