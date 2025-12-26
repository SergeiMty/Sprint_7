from api.endpoints import ORDERS_LIST


class TestOrdersList:
    def test_orders_list_returns_orders(self, api):
        r = api.get(ORDERS_LIST)
        assert r.status_code == 200

        body = r.json()
        assert "orders" in body
        assert isinstance(body["orders"], list)

