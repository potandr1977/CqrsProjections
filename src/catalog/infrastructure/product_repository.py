from sqlalchemy.ext.asyncio import AsyncEngine


class ProductRepository:
    def __init__(self): #, engine: AsyncEngine):
        self.name = "ProductRepName"

    def get_name(self):
        return self.name