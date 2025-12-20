import pytest
from api.endpoints import ORDERS_CREATE
from api.payloads import order_payload

@pytest.mark.parametrize(
    "colors",
    [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        None,  # не указываем поле color вообще
    ],
    ids=["black", "grey", "both", "no_color"]
)
def test_create_order_returns_track(api, colors):
    payload = order_payload(colors)
    r = api.post(ORDERS_CREATE, json=payload)

    assert r.status_code == 201
    body = r.json()
    assert "track" in body
    assert body["track"] is not None
