# Представим, что вместо принтов тут вызовы внешних сервисов:
# inventory_service, payment_service, shipping_service и т.п.
from typing import Dict

def create_payment(ctx: Dict):
    if ctx.get("force_inventory_fail"):
        raise RuntimeError("Не удалось зарезервировать товар")
    # обычно тут вернётся id резерва или что-то подобное
    return {"reservation_id": 123}


def compensate_create_payment(ctx: Dict):
    reservation = ctx.get("reserve_stock")
    if reservation:
        # вызвать inventory_service.cancel_reservation(reservation["reservation_id"])
        pass