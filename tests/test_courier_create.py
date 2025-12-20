import pytest
from api.endpoints import COURIER_CREATE
from api.payloads import courier_payload

def test_create_courier_success(api, created_courier):
    _, r = created_courier
    assert r.status_code == 201
    assert r.json() == {"ok": True}

def test_cant_create_duplicate_courier(api, courier_data):
    r1 = api.post(COURIER_CREATE, json=courier_data)
    assert r1.status_code == 201

    r2 = api.post(COURIER_CREATE, json=courier_data)
    # обычно 409
    assert r2.status_code in (400, 409)
    body = r2.json()
    assert "message" in body  # не привязываемся к тексту, чтобы не упасть от формулировки

@pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
def test_create_courier_missing_required_field(api, missing_field):
    data = courier_payload()
    data.pop(missing_field)

    r = api.post(COURIER_CREATE, json=data)
    assert r.status_code == 400
    assert "message" in r.json()
