import os

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine

from app.constants import BASE_DIR
from app.db import get_session
from app.main import app


@pytest.fixture(name="session")
def session_fixture():
    db_name = "testing.db"
    engine = create_engine(
        f"sqlite:///{db_name}", connect_args={"check_same_thread": False}
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

    os.remove(BASE_DIR / db_name)


@pytest.fixture(name="client")  #
def client_fixture(session: Session):
    def get_session_override():  #
        return session

    app.dependency_overrides[get_session] = get_session_override  #

    client = TestClient(app)  #
    yield client  #
    app.dependency_overrides.clear()
