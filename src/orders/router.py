from fastapi import APIRouter, Depends


router = APIRouter(prefix="/orders", tags=["orders"])

@router.get(
    '/ping',
    responses={400: {"description": "Bad request"}},
    description="Проверяем жизнеспособность сервиса заказов",
)
async def ping():
    return "pong"

