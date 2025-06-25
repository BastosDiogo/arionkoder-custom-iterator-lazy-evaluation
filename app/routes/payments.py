from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from services.payments_process import Payments
from fastapi.encoders import jsonable_encoder

router = APIRouter(tags=["Payments"], prefix="/payments")

@router.get("/all")
def all(page:int = 1, page_size:int = 10):
    """Retun all mock Payments.
    \nParameters:
    \n`page`: Specifies the current page number for pagination. Format `int`;
    \n`page_size`: Defines the maximum number of objects to return per page. Format `int`.
    """

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(Payments().all_payments(page, page_size))
    )

@router.get("/payments-created-month")
def payments_created_month(month:int, page:int = 1, page_size:int = 10):
    """Return all payments equal or below 'month' parameters.
    \nParameters:
    \n`month`: The numerical representation of the month (e.g., 1 for January, 2 for February). Format `int`
    \n`page`: Specifies the current page number for pagination. Format `int`;
    \n`page_size`: Defines the maximum number of objects to return per page. Format `int`.
    """

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(Payments().created_before_month(month, page, page_size))
    )


@router.get("/trimestal-payments")
def trimestal_payments():
    """Return payments per trimestre."""
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(Payments().trimestal_payments())
    )


@router.get("/payment-groups")
def payment_groups(group_size:int, page:int=1, page_size:int=10):
    """Return payments per trimestre.
    \nParameters:
    \n`group_size`: Size of group. Format `int`
    \n`page`: Specifies the current page number for pagination. Format `int`;
    \n`page_size`: Defines the maximum number of objects to return per page. Format `int`.
    """
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(Payments().payment_groups(group_size, page, page_size))
    )