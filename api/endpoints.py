BASE_URL = "https://qa-scooter.praktikum-services.ru"  # проверь, что в задании у тебя именно этот URL

COURIER_CREATE = "/api/v1/courier"
COURIER_LOGIN = "/api/v1/courier/login"
COURIER_DELETE = "/api/v1/courier/{courier_id}"

ORDERS_CREATE = "/api/v1/orders"
ORDERS_LIST = "/api/v1/orders"
ORDER_TRACK = "/api/v1/orders/track"          # ?t=TRACK
ORDER_ACCEPT = "/api/v1/orders/accept/{order_id}"  # ?courierId=ID
