# coding: utf-8

from starlette.testclient import TestClient
from app import api, _STYLE_NAMES



def test_get_greeting():
    with TestClient(api) as client:
        rsp = client.get("/api/v1/greet?name=Barry")
        assert rsp.status_code == 200
        data =  rsp.json()
        assert 'Barry' in data['greeting']
        assert data['name'] == 'Barry'
        assert data['style'] in _STYLE_NAMES


def test_get_greeting_without_user_returns_422():
    with TestClient(api) as client:
        rsp = client.get("/api/v1/greet")
        assert rsp.status_code == 422
        assert rsp.json() == {
            "detail": [
                {
                    "loc": ["query", "name"],
                    "msg": "field required",
                    "type": "value_error.missing",
                }
            ]
        }
