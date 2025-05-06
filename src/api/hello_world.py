from fastapi import APIRouter

router = APIRouter()

@router.get(
    "/hello-world",
    status_code=200
)
async def hello_world():
    return {"message": "Hello, World!"}