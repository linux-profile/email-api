from fastapi import APIRouter


router = APIRouter()


@router.get("/email", status_code=200)
async def get():
    return [{}]


@router.get("/email/{id}", status_code=200)
def get_by_id(id: int):
    return {}
