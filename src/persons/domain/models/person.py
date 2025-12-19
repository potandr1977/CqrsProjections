import decimal
from dataclasses import dataclass

@dataclass
class Person:
    id: str
    name:str
    inn:str
    saldo:decimal.Decimal = 0