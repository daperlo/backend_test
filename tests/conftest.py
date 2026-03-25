import pytest
from fastapi.testclient import TestClient

from app.main import app

# 🔥 ОТКЛЮЧАЕМ AUTH (если он есть)
# ВАЖНО: импортируй свою зависимость get_current_user
try:
    from app.auth.dependencies import get_current_user

    def override_get_current_user():
        return {"id": 1, "email": "test@test.com"}

    app.dependency_overrides[get_current_user] = override_get_current_user

except ImportError:
    # если у тебя нет auth dependency — просто игнор
    pass


@pytest.fixture
def client():
    return TestClient(app)