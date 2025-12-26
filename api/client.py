import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


DEFAULT_TIMEOUT = (5, 30)  


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

        retry = Retry(
            total=3,
            connect=3,
            read=3,
            status=3,
            backoff_factor=0.5,
            status_forcelist=(500, 502, 503, 504),
            allowed_methods=frozenset(["GET"]),
            raise_on_status=False,
        )
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def post(self, path: str, json=None, params=None, timeout=DEFAULT_TIMEOUT):
        return self.session.post(
            f"{self.base_url}{path}",
            json=json,
            params=params,
            timeout=timeout,
        )

    def get(self, path: str, params=None, timeout=DEFAULT_TIMEOUT):
        return self.session.get(
            f"{self.base_url}{path}",
            params=params,
            timeout=timeout,
        )

