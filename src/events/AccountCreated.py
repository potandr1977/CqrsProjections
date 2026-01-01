import json
from dataclasses import dataclass


@dataclass
class AccountCreated:
    id: str
    person_id:str
    name:str

    @classmethod
    def from_json(cls, json_str:str):
        data = json.loads(json_str)
        return cls(id=data["id"],person_id=data["person_id"],name=data["name"])