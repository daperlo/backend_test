from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "supersecretkey"  # потом можно в env
ALGORITHM = "HS256"


def create_token(user_id: str, role: str):
    payload = {
        "user_id": user_id,
        "role": role,
        "exp": datetime.utcnow() + timedelta(hours=12)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])