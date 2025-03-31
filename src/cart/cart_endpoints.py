from typing import Annotated

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.cart.cart_container import CartContainer
from src.cart.domain.cart_service_interface import ICartService

router = APIRouter(prefix="/carts", tags=["cart"])

@router.get(
    '/ping',
    responses={400: {"description": "Bad request"}},
    description="Проверяем жизнеспособность сервиса корзины",
)
async def ping():
    return "pong"

@router.get("/cart")
@inject
async def catalog(cart_service: Annotated[ICartService, Depends(Provide[CartContainer.service])]):
    name = cart_service.get_rep_name()
    return name