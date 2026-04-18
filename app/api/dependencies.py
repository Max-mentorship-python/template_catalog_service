# from sqlalchemy.orm import Session

from app.core.database import SessionLocal


def get_db():
    """Dependency для получения сессии БД в эндпоинтах FastAPI."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
