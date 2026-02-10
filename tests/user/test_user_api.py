import uuid
from fastapi import status
from tests.factory.user_factory import login_payload
from tests.factory.user_factory import register_payload


def test_login_user(client):
    response = client.post("/login",json=login_payload())
    
    assert response.status_code ==status.HTTP_200_OK
    data=response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_register_user(client):
    response = client.post("/register",json={"firstname":"admin",
                                             "lastname":"lastname",
                                             "email": f"{uuid.uuid4()}@test.com",
                                             "password":"123456"}
)
    assert response.status_code == 201