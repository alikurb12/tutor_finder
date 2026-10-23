import bcrypt
from datetime import datetime, timedelta, timezone
import jwt

from app.config.config import settings

ALGORITHM = "HS256"

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password: str, password_hash: str) -> bool:
    return bcrypt.checkpw(password.encode(), password_hash.encode())

def _create_token(user_id: int, token_type: str, lifetime: timedelta) -> str:
    payload = {
        "sub" : str(user_id),
        "type": token_type,
        "exp" : datetime.now(timezone.utc) + lifetime
    }

    return jwt.encode(payload, settings.secret_key, algorithm=ALGORITHM)


def create_access_token(user_id: int) -> str:
    return _create_token(user_id, "access", timedelta(minutes=settings.access_token_minutes))

def create_refresh_token(user_id: int) -> str:
    return _create_token(user_id, "refresh", timedelta(days=settings.refresh_token_days))

def decode_token(token: str, expected_type: str) -> int:
    payload = jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
    if payload.get("type") != expected_type:
        raise jwt.InvalidTokenError("Неверный тип токена")
    return int(payload["sub"])