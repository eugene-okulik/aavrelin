import pytest
import requests
import allure


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
    with allure.step("Создаем объект методом post"):
        body = {"name": "Новый объект", "data": {"объект": "ВОЗДУХ"}}
        headers = {"Content-Type": "application/json"}
        response = requests.post(
            "http://167.172.172.115:52353/object", json=body, headers=headers
        )
        post_id_for_test = response.json()["id"]
        yield post_id_for_test
        with allure.step("Удаление тестовых данных"):
            requests.delete(f"http://167.172.172.115:52353/object/{post_id_for_test}")


@pytest.fixture()
def create_object():
    with allure.step("Создаем объект для теста"):
        body = {"name": "Новый объект", "data": {"объект": "ВОЗДУХ"}}
        headers = {"Content-Type": "application/json"}
        response = requests.post(
            "http://167.172.172.115:52353/object", json=body, headers=headers
        )
        post_id_for_test = response.json()["id"]
        return post_id_for_test
