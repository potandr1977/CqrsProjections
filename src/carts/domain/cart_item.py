from dataclasses import dataclass

from src.products.domain.product import Product


@dataclass
class CartItem:
    product: Product
    amount: int