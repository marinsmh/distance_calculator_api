import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture()
def client():
    return TestClient(app)


def test_distance_200_OK(client):
    response = client.get("/distance?origin=1600 Amphitheatre Parkway, Mountain View, CA&destination=1 Infinite Loop, "
                          "Cupertino, CA&mode=driving&units=metric")
    assert response.status_code == 200
    assert response.json() == {"distance": "15.8 km", "duration": "16 mins"}


def test_distance_422(client):
    response = client.get("/distance?destination=1 Infinite Loop, Cupertino, CA&mode=driving&units=metric")
    assert response.status_code == 422
    assert response.json() == {"detail": [{"loc": ["query", "origin"], "msg": "field required", "type": "value_error"
                                                                                                        ".missing"}]}


def test_distance_400(client):
    origin = "Narnia"
    destination = "Hogwarts"
    response = client.get(f"/distance?origin={origin}&destination={destination}&mode=driving&units=metric")
    assert response.status_code == 400


def test_api_404(client):
    response = client.get("/not_found")
    assert response.status_code == 404
