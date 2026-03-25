import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.db.base import Base
from app.db.session import get_db

# тестовая БД (ВАЖНО: она должна существовать в Postgres)
TEST_DB_URL = "postgresql://postgres:postgres@localhost:5432/app_test_db"

engine = create_engine(TEST_DB_URL, echo=False)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# создаём таблицы 1 раз на всю сессию тестов
@pytest.fixture(scope="session", autouse=True)
def prepare_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


# override зависимости FastAPI
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


# тестовый клиент
@pytest.fixture()
def client():
    with TestClient(app) as c:
        yield c