from api.endpoints import ORDERS_LIST

def test_orders_list_returns_orders(api):
    r = api.get(ORDERS_LIST)
    assert r.status_code == 200
    body = r.json()
    assert "orders" in body
    assert isinstance(body["orders"], list)
