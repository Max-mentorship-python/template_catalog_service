from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.models import Order
from app.schemas import OrderCreate, OrderResponse

router = APIRouter()