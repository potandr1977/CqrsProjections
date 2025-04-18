from fastapi import APIRouter, Depends

router = APIRouter(prefix="/payments", tags=["payments"])

@router.get(
    '/ping',
    responses={400: {"description": "Bad request"}},
    description="Проверяем жизнеспособность сервиса платежей",
)
async def ping():
    return "pong"

