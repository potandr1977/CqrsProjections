import decimal
from dataclasses import dataclass

@dataclass
class Account:
    id:str
    name:str
    saldo:decimal.Decimal
