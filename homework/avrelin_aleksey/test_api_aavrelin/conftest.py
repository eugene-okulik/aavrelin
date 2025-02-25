import pytest
import requests
import allure
import dotenv
import json
import os

from test_api_aavrelin.endpoints.create_post import CreatePost
from test_api_aavrelin.endpoints.update_post import UpdatePost
from test_api_aavrelin.endpoints.delete_post import DeletePost
from test_api_aavrelin.endpoints.get_post import GetPost
from test_api_aavrelin.endpoints.check_status_code import StatusCode


dotenv.load_dotenv()
BASE_URL = os.getenv("BASE_URL")
HEADERS = json.loads(os.getenv("HEADERS"))


@pytest.fixture(scope="session")
def start_end_message():
    print("\nStart testing")
    yield
    print("\nTesting completed")


@pytest.fixture()
def print_before_after_every_test():
    print("\nbefore test")
    yield
    print("\nafter test")


@pytest.fixture()
def create_and_delete_object():

    with allure.step("Создаем объект методом POST"):
        body = {"name": "Новый объект", "data": {"объект": "ВОЗДУХ"}}
        response = requests.post(
            BASE_URL,
            json=body,
            headers=HEADERS)
        post_id = response.json()["id"]

        yield post_id

        with allure.step("Удаление тестовых данных"):
            requests.delete(f"{BASE_URL}/{post_id}")


@pytest.fixture()
def create_object():
    with allure.step("Создаем объект для теста"):
        body = {"name": "Новый объект", "data": {"объект": "ВОЗДУХ"}}
        response = requests.post(
            BASE_URL,
            json=body,
            headers=HEADERS
        )
        post_id = response.json()["id"]
        return post_id


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()


@pytest.fixture()
def delete_post_endpoint():
    return DeletePost()


@pytest.fixture()
def get_post_endpoint():
    return GetPost()


@pytest.fixture()
def check_post_test_status_code(create_post_endpoint):
    return StatusCode(create_post_endpoint)


@pytest.fixture()
def check_delete_test_status_code(delete_post_endpoint):
    return StatusCode(delete_post_endpoint)


@pytest.fixture()
def check_get_test_status_code(get_post_endpoint):
    return StatusCode(get_post_endpoint)


@pytest.fixture()
def check_update_test_status_code(update_post_endpoint):
    return StatusCode(update_post_endpoint)


@pytest.fixture
def post_id_for_put():
    return 42
