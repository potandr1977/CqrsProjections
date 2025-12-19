import decimal
from dataclasses import dataclass


@dataclass
class PersonCreated:
    id: str
    name:str
    inn:str