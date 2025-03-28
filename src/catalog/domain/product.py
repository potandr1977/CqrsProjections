import queue
from dataclasses import dataclass
from datetime import datetime

from src.catalog.domain.category import Category
from src.catalog.domain.price import Price
from src.catalog.domain.product_feature import ProductFeature


@dataclass(repr=False)
class Product:
    id: int
    name: str
    description: str
    categories: list[Category]
    price_history: queue.Queue[Price](maxsize=10)

    @property
    def get_aсtual_price(self) -> tuple[Price, ...]:
        res = [Price(datetime(2025,1,2),123), Price(datetime(2025,2,3),144)]
        return tuple(res)

    @property
    def get_features(self) -> tuple[ProductFeature, ...]:
        res = [Price(datetime(2025, 1, 2), 123), Price(datetime(2025, 2, 3), 144)]
        return tuple(res)



