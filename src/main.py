import uvicorn
from fastapi import FastAPI

from products.catalog_endpoints import router as catalog_router
from carts.cart_endpoints import router as cart_router
from src.carts.cart_container import CartContainer
from src.products.catalog_container import CatalogContainer


def create_app() -> FastAPI:
    catalog_container = CatalogContainer()
    cart_container = CartContainer()

    app = FastAPI()
    app.catalog_container = catalog_container
    app.cart_container = cart_container

    app.include_router(catalog_router)
    app.include_router(cart_router)
    #app.include_router(payment_router)
    #app.include_router(reports_router)

    return app

app = create_app()

if __name__ == "__main__":
    _port = 3003
    print(f"http://127.0.0.1:{_port}/docs")
    uvicorn.run(app, port = _port)