from fastapi import FastAPI
from app.db.database import crear_tablas

app = FastAPI(lifespan=crear_tablas)

@app.get("/")
def get_root():
    return {"Hello":"World"}