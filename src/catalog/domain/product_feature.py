from dataclasses import dataclass


@dataclass(frozen=True)
class ProductFeature:
    name: str
    value: int