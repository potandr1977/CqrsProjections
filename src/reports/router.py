from fastapi import APIRouter, Depends


router = APIRouter(prefix="/reports", tags=["report"])

@router.get(
    '/ping',
    responses={400: {"description": "Bad request"}},
    description="Проверяем жизнеспособность сервиса отчётов",
)
async def ping():
    return "pong"

