from dependency_injector.wiring import inject
from fastapi import APIRouter, Depends


router = APIRouter(prefix="/carts", tags=["cart"])

@router.get(
    '/ping',
    responses={400: {"description": "Bad request"}},
    description="Проверяем жизнеспособность сервиса корзины",
)
async def ping():
    return "pong"

@router.get("/catalog")
@inject
async def catalog(product_service: Annotated[ProductService, Depends(Provide[CatalogContainer.service])]):
    name = product_service.get_rep_name()
    return name

