from fastapi import FastAPI

from app.api.routes import router

# Создаем экземпляр приложения FastAPI
# Параметр title задает название сервиса (отображается в Swagger-документации)
app = FastAPI(title="Catalog Service")

app.include_router(router)
