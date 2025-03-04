import requests
import allure
import dotenv
import os
import json
from faker import Faker


dotenv.load_dotenv()
BASE_URL = os.getenv("BASE_URL")
HEADERS = json.loads(os.getenv("HEADERS"))
USER_NAME = os.getenv("USER_NAME")


fake = Faker()

memes_data = {
    "text": fake.sentence(),
    "url": fake.image_url(),
    "tags": [fake.word() for _ in range(3)],
    "info": {"key": fake.uuid4()},
}



class BaseEndpoint:
    def __init__(self):
        self.url = BASE_URL
        self.headers = HEADERS
        self.response = None

    @allure.step("Проверка статус-кода")
    def check_status_code(self, code):
        assert self.response.status_code == code


class Authorization(BaseEndpoint):
    @allure.step("Авторизация пользователя")
    def authorization_user(self, name):
        self.response = requests.post(
            f"{self.url}/authorize", json={"name": name}, headers=self.headers
        )
        return self.response.json()["token"]
