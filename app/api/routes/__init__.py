# Агрегируем все роутеры сервиса в один объект.
# Добавляйте сюда новые роутеры по мере расширения сервиса.
from fastapi import APIRouter

from app.api.routes.products import router as products_router

router = APIRouter()

router.include_router(products_router, prefix="/products", tags=["products"])
