import allure
import dotenv
import json
import os


dotenv.load_dotenv()
BASE_URL = os.getenv("BASE_URL")
HEADERS = json.loads(os.getenv("HEADERS"))


class Endpoint():
    url = BASE_URL
    headers = HEADERS
    response = None
    json = None

    def __init__(self):
        self.response = None
