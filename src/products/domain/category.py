from dataclasses import dataclass


@dataclass(frozen=True)
class Category:
    id: int
    parent_category_id: int
    category_name: str
