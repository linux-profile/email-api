from fastapi import APIRouter
from app.api.v1.endpoints import email


v1 = APIRouter()
v1.include_router(email.router, tags=["Email"])
