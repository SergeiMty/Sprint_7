import pytest

from api.endpoints import COURIER_LOGIN
from api.payloads import courier_login_payload


class TestCourierLogin:
    def test_courier_can_login(self, api, created_courier):
        courier, _ = created_courier

        r = api.post(COURIER_LOGIN, json=courier_login_payload(courier))
        assert r.status_code == 200

        body = r.json()
        assert "id" in body
        assert isinstance(body["id"], int)

    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_missing_required_field(self, api, created_courier, missing_field):
        courier, _ = created_courier

        data = courier_login_payload(courier)
        data[missing_field] = ""  

        r = api.post(COURIER_LOGIN, json=data)
        assert r.status_code == 400
        assert "message" in r.json()

    def test_login_wrong_password(self, api, created_courier):
        courier, _ = created_courier

        data = courier_login_payload(courier)
        data["password"] = "wrong_password"

        r = api.post(COURIER_LOGIN, json=data)
        assert r.status_code in (400, 404)
        assert "message" in r.json()

    def test_login_nonexistent_user(self, api):
        r = api.post(COURIER_LOGIN, json={"login": "no_such_login_123", "password": "none"})
        assert r.status_code in (400, 404)
        assert "message" in r.json()


