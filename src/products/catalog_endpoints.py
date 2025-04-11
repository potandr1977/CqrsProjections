from typing import Annotated

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.products.catalog_container import CatalogContainer
from src.products.domain.product_service_interface import IProductService

router = APIRouter(prefix="/catalogs", tags=["products"])

@router.get(
    '/ping',
    responses={400: {"description": "Bad request"}},
    description="Проверяем жизнеспособность сервиса каталога",
)
async def ping():
    return "pong"

@router.get("/products")
@inject
async def catalog(product_service: Annotated[IProductService, Depends(Provide[CatalogContainer.service])]):
    name = product_service.get_rep_name()
    return name

