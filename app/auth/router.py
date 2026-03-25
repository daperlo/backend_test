from fastapi import APIRouter
from app.auth.jwt import create_token
import uuid

router = APIRouter()


@router.post("/dummyLogin")
def dummy_login(role: str):
    if role == "admin":
        user_id = "00000000-0000-0000-0000-000000000001"
    else:
        user_id = "00000000-0000-0000-0000-000000000002"

    token = create_token(user_id, role)

    return {
        "access_token": token,
        "token_type": "bearer"
    }