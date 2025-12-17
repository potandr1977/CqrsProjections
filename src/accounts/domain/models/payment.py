import decimal
from dataclasses import dataclass

@dataclass
class Payment:
    id:str
    purpose:str
    sum:decimal.Decimal
