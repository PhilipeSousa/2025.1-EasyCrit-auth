from fastapi import APIRouter
from app.routers.routes.users import router as user_router
from app.routers.routes.auth import router as auth_router

api_router = APIRouter()
api_router.include_router(user_router)
api_router.include_router(auth_router)
