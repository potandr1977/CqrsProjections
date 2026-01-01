import decimal
import json
from dataclasses import dataclass


@dataclass
class PaymentCreated:
    id: str
    account_id:str
    sum: decimal.Decimal

    @classmethod
    def from_json(cls, json_str:str):
        data = json.loads(json_str)
        return cls(id=data["id"],account_id=data["account_id"],sum=data["sum"])