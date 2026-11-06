from sqlmodel import select
from app.models.producto import Producto

def obtener_productos(user_id: int, session):
    consulta = select(Producto).where(
        Producto.user_id == user_id
    )

    return session.exec(consulta).all()