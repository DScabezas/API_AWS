from fastapi import APIRouter
from app.db.database import SessionDep
from app.services import producto_service
from app.dependencies.auth import CurrentUser

router = APIRouter(tags=["Producto"], prefix="/productos")

@router.get("/")
def obtener_productos(
    current_user: CurrentUser, 
    session: SessionDep
):
    return producto_service.obtener_productos(
        current_user.id,
        session
    )