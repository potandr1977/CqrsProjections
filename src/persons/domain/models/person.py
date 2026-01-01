import decimal
from dataclasses import dataclass, field
from typing import List

from src.persons.domain.models.account import Account


@dataclass
class Person:
    id: str
    name:str
    inn:str
    accounts:List[Account] = field(default_factory=list)
    saldo:decimal.Decimal = 0

