from dataclasses import field
from typing import List

from pydantic.dataclasses import dataclass
from src.accounts.domain.models.payment import Payment
from src.accounts.domain.models.person import Person


@dataclass
class Account:
    id: str
    name: str
    person: Person
    payments: List[Payment] = field(default_factory=list)

