import uvicorn
from fastapi import FastAPI

from catalog.catalog_endpoints import router as catalog_router
from order.router import router as order_router
from payment.router import router as payment_router
from reports.router import router as reports_router
from src.catalog.catalog_container import CatalogContainer


def create_app() -> FastAPI:
    catalog_container = CatalogContainer()

    app = FastAPI()
    app.container = catalog_container

    app.include_router(catalog_router)
    #app.include_router(order_router)
    #app.include_router(payment_router)
    #app.include_router(reports_router)

    return app

app = create_app()

if __name__ == "__main__":
    _port = 3003
    print(f"http://127.0.0.1:{_port}/docs")
    uvicorn.run(app, port = _port)