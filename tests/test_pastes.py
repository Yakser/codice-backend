from fastapi.testclient import TestClient
from sqlmodel import Session

from .fixtures import session_fixture, client_fixture  # noqa: F401


def test_create_paste(session: Session, client: TestClient):
    response = client.post(
        "/pastes/",
        json={
            "slug": "test_slug",
            "author": "test_author",
            "content": "test_content",
            "title": "test_title",
            "description": "test_description",
            "language": "test_language",
        },
    )
    data = response.json()

    assert response.status_code == 200
    assert data["id"] is not None
    assert data["slug"] == "test_slug"
    assert data["content"] == "test_content"
    assert data["title"] == "test_title"
    assert data["description"] == "test_description"
    assert data["language"] == "test_language"
