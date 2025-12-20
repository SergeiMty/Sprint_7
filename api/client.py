import requests
from api.endpoints import BASE_URL

class ApiClient:
    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url.rstrip("/")

    def post(self, path: str, json: dict | None = None, params: dict | None = None):
        return requests.post(self.base_url + path, json=json, params=params, timeout=10)

    def get(self, path: str, params: dict | None = None):
        return requests.get(self.base_url + path, params=params, timeout=10)

    def put(self, path: str, params: dict | None = None, json: dict | None = None):
        return requests.put(self.base_url + path, params=params, json=json, timeout=10)

    def delete(self, path: str):
        return requests.delete(self.base_url + path, timeout=10)
