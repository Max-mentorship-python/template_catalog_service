# Агрегируем все роутеры сервиса в один объект.
# Добавляйте сюда новые роутеры по мере расширения сервиса.
from fastapi import APIRouter

from app.api.routes.orders import router as orders_router

router = APIRouter()

router.include_router(orders_router, prefix="/orders", tags=["orders"])
