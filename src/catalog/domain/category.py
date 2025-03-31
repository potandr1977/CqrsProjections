from dataclasses import dataclass


@dataclass
class Category(frozen=True):
    id: int
    parent_category_id: int
    name: str
