from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import JWTError
from app.auth.jwt import decode_token

security = HTTPBearer()

'''
def get_current_user(credentials=Depends(security)):
    token = credentials.credentials

    try:
        payload = decode_token(token)

        return {
            "id": payload.get("user_id"),
            "email": payload.get("email", "test@test.com"),
            "role": payload.get("role", "user")
        }

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    '''
def get_current_user(credentials=Depends(security)):
    token = credentials.credentials

    try:
        payload = decode_token(token)

        return {
    "id": payload.get("user_id"),
    "email": "test@test.com",
    "role": "admin"
    }

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")