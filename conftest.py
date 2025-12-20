import pytest
from api.client import ApiClient
from api.payloads import courier_payload, courier_login_payload
from api.endpoints import COURIER_CREATE, COURIER_LOGIN, COURIER_DELETE

@pytest.fixture()
def api():
    return ApiClient()

@pytest.fixture()
def courier_data():
    return courier_payload()

@pytest.fixture()
def created_courier(api, courier_data):
    # создаём курьера
    r = api.post(COURIER_CREATE, json=courier_data)
    yield courier_data, r

    # cleanup: логинимся -> получаем id -> удаляем
    login_r = api.post(COURIER_LOGIN, json=courier_login_payload(courier_data))
    if login_r.status_code == 200:
        courier_id = login_r.json().get("id")
        if courier_id:
            api.delete(COURIER_DELETE.format(courier_id=courier_id))
