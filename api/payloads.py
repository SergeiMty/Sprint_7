from faker import Faker

fake = Faker("en_US")  

def courier_payload() -> dict:
    
    login = f"serg_{fake.user_name()}_{fake.pyint(min_value=1000, max_value=9999)}"
    password = fake.password(length=10)
    first_name = fake.first_name()
    return {
        "login": login,
        "password": password,
        "firstName": first_name
    }

def courier_login_payload(courier: dict) -> dict:
    return {"login": courier["login"], "password": courier["password"]}

def order_payload(colors: list[str] | None):
    payload = {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.street_address(),
        "metroStation": 4,
        "phone": "+79990001122",
        "rentTime": 2,
        "deliveryDate": "2025-12-25",
        "comment": "Test order",
    }
    
    if colors is not None:
        payload["color"] = colors
    return payload
