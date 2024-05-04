from fastapi import APIRouter, Depends

from app.core.database import get_db


router = APIRouter()


@router.get("/email", status_code=200)
async def get(db=Depends(get_db)):
    return [{}]


@router.get("/email/{id}", status_code=200)
def get_by_id(id: int, db=Depends(get_db)):
    return {}


@router.post("/email", status_code=201)
async def post(db=Depends(get_db)):
    return {}
