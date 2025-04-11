from typing import Annotated

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.carts.cart_container import CartContainer
from src.carts.domain.cart_service_interface import ICartService

router = APIRouter(prefix="/carts", tags=["carts"])

@router.get(
    '/ping',
    responses={400: {"description": "Bad request"}},
    description="Проверяем жизнеспособность сервиса корзины",
)
async def ping():
    return "pong"

@router.get("/carts")
@inject
async def catalog(cart_service: Annotated[ICartService, Depends(Provide[CartContainer.service])]):
    name = cart_service.get_rep_name()
    return name