import pytest
from fastapi.testclient import TestClient
from app.db.session import engine
from app.db.base import Base
from app.main import app
from app.db.session import SessionLocal
from app.auth.dependencies import get_current_user

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

# ---- TEST DB OVERRIDE ----
def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---- TEST USER OVERRIDE ----
def override_get_current_user():
    return {
        "id": 1,
        "email": "test@test.com",
        "role": "admin"
    }


@pytest.fixture
def client():
    app.dependency_overrides[get_current_user] = override_get_current_user
    app.dependency_overrides[SessionLocal] = override_get_db  # (не обязательно)

    # ВАЖНО: именно так правильно переопределять get_db
    from app.db.session import get_db
    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as c:
        yield c

    app.dependency_overrides.clear()