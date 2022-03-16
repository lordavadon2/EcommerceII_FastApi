from datetime import datetime

from sqlalchemy.orm import Session
from starlette import status
from starlette.requests import Request
from starlette.responses import RedirectResponse

from src.app.coupon import crud


def coupon_apply(request: Request,
                   code: str,
                   db: Session):

    now = datetime.now()
    try:
        coupon = crud.get_coupon(db, code, now)
        request.session['coupon_id'] = coupon.id
    except:
        request.session['coupon_id'] = None
    return RedirectResponse(url='/cart', status_code=status.HTTP_303_SEE_OTHER)
