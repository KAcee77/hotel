from fastapi import APIRouter

from . import (
    auth,
    hotel,
)


router = APIRouter()
router.include_router(auth.router)
router.include_router(hotel.router)
