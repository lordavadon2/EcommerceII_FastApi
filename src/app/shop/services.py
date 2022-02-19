from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status
from starlette.requests import Request

from src.utils.depencies import templates, env
from src.app.shop import crud


def get_all_data(request: Request, category_slug: str = '', db: Session = None, page: int = 1):
    products = crud.product_list(category_slug=category_slug, db=db)[16 * (page - 1):16 * page]
    categories = crud.category_list(db=db)
    category = crud.get_category_by_slug(category_slug=category_slug, db=db)

    return templates.TemplateResponse(env.get_template('list.html'),
                                      {
                                          'request': request,
                                          'page': page,
                                          'products': products,
                                          'categories': categories,
                                          'category': category,
                                      })


def product_detail(request: Request, product_id: int, product_slug: str, db: Session):
    product = crud.product_detail(id=product_id, slug=product_slug, db=db)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found...")
    return templates.TemplateResponse(env.get_template('detail.html'),
                                      {
                                          'request': request,
                                          'product': product
                                      })
