import queue
from dataclasses import dataclass
from datetime import datetime
from typing import Tuple, Final

from src.catalog.domain.category import Category
from src.catalog.domain.price import Price

PRICE_MAX_SIZE: Final[int] = 10

@dataclass(repr=False)
class Product:
    id: int
    name: str
    description: str
    categories: list[Category]
    base_price_history: queue.Queue[Price](maxsize=PRICE_MAX_SIZE)

    @property
    def get_prices(self) -> tuple[Price, ...]:
        return tuple(self.base_price_history)

    def add_price(self, price:Price):
        self.base_price_history.append(price)

