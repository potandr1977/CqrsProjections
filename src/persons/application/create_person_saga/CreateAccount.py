# Представим, что вместо принтов тут вызовы внешних сервисов:
# inventory_service, payment_service, shipping_service и т.п.
from typing import Dict

def create_account(ctx: Dict):
    if ctx.get(""):
        raise RuntimeError("Не удалось зарезервировать товар")
    return {"reservation_id": 123}


def compensate_create_account(ctx: Dict):
    if ctx.get(""):
        raise RuntimeError("Не удалось зарезервировать товар")
    reservation = ctx.get("reserve_stock")
