from fastapi import FastAPI
from app.db.database import crear_tablas
from app.controllers.producto_controller import router as producto_router

app = FastAPI(lifespan=crear_tablas)

app.include_router(producto_router)
