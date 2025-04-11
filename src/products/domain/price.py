from dataclasses import dataclass
from datetime import datetime

from unicodedata import decimal


@dataclass(frozen=True)
class Price:
    product_id: int
    date: datetime
    value: decimal
