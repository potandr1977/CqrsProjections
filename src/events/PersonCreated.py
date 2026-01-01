import json
from dataclasses import dataclass


@dataclass
class PersonCreated:
    id: str
    name:str
    inn:str

    @classmethod
    def from_json(cls, json_str:str):
        data = json.loads(json_str)
        return cls(id=data["id"],name=data["name"],inn=data["inn"])