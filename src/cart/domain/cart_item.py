from dataclasses import dataclass

from src.catalog.domain.product import Product


@dataclass
class CartItem:
    product: Product
    amount: int