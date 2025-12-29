import decimal
from dataclasses import dataclass
from typing import List

from src.persons.domain.models.account import Account


@dataclass
class Person:
    id: str
    name:str
    inn:str
    accounts:List[Account]
    saldo:decimal.Decimal = 0