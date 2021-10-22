import os

SUBSCRIPTION_API_HOST = os.getenv("SUBSCRIPTION_HOST", "localhost")
SUBSCRIPTION_API_PORT = os.getenv("SUBSCRIPTION_PORT", "8001")

SUBSCRIPTION_API_URL = f"{SUBSCRIPTION_API_HOST}:{SUBSCRIPTION_API_PORT}"
SUBSCRIPTION_API_VERSION = "v1"

PAYMENTS_API_HOST = os.getenv("PAYMENTS_HOST", "localhost")
PAYMENTS_API_PORT = os.getenv("PAYMENTS_PORT", "8000")

PAYMENTS_API_URL = f"{PAYMENTS_API_HOST}:{PAYMENTS_API_PORT}"
PAYMENTS_API_VERSION = "v1"

ALGORITHM = "HS256"
SECRET_KEY = "super-secret"
USER_ID = 'a49b436a-d0b3-4e3e-84e5-ac9204a33042'
