import requests
import pytest
import allure
import dotenv
import os


dotenv.load_dotenv()
http_url_portal = os.getenv("BASE_URL")


@allure.feature("Posts")
@allure.story("Get posts")
@allure.title("Получение информации по всем объектам")
@pytest.mark.smoke
def test_get_all(start_end_message, print_before_after_every_test):
    with allure.step("Отправка запроса get"):
        response = requests.get(http_url_portal)

    with allure.step("Проверка статус кода ответа = 200"):
        assert response.status_code == 200

    with allure.step("Печатаем результат"):
        with allure.step("Печатаем результат"):
            allure.attach(
                str(response.json()),
                name="Response_json_file",
                attachment_type=allure.attachment_type.JSON,
            )


@allure.feature("Posts")
@allure.story("Create posts")
@pytest.mark.smoke
@pytest.mark.parametrize(
    "body",
    [
        {"name": "Важное", "data": {"объект": "ВОЗДУХ"}},
        {"name": "Техника", "data": {"Машина1": "БМВ", "Машина2": "Мерседес"}},
        {"name": "", "data": {"Деньги": "наличные"}},
    ],
)
def test_post(body):
    headers = {"Content-Type": "application/json"}
    with allure.step("Создаем объект методом post"):
        response = requests.post(http_url_portal, json=body, headers=headers)
    with allure.step("Проверка статус кода ответа = 200"):
        assert response.status_code == 200
    post_id = response.json()["id"]
    with allure.step("Удаление тестовых данных"):
        requests.delete(f"{http_url_portal}/{post_id}")


@allure.feature("Posts")
@allure.story("Get posts")
@pytest.mark.skip
@pytest.mark.smoke
def test_get_one(print_before_after_every_test, create_and_delete_object):
    response = requests.get(f"{http_url_portal}/{create_and_delete_object}")
    with allure.step("Проверка статус кода ответа = 200"):
        assert response.status_code == 200, "Сведения об объекте отсутствуют"
    with allure.step("Печатаем результат"):
        print(response.json())


@allure.feature("Posts")
@allure.story("Change posts")
@pytest.mark.smoke
@pytest.mark.medium
def test_put(print_before_after_every_test, create_and_delete_object):
    with allure.step("Выполнения запроса полного изменения put"):
        body = {
            "name": "Новые объекты",
            "data": {"стихия_1": "Вода", "стихия_2": "Земля"},
        }
        headers = {"Content-Type": "application/json"}
        response = requests.put(
            f"{http_url_portal}/{create_and_delete_object}", json=body, headers=headers
        )
    with allure.step("Проверка статус кода ответа = 200"):
        assert response.status_code == 200, "Объект не изменен"
    with allure.step("Печатаем результат"):
        print(response.json())


@allure.feature("Posts")
@allure.story("Change posts")
@pytest.mark.smoke
@pytest.mark.critical
def test_patch(print_before_after_every_test, create_and_delete_object):
    with allure.step("Выполнения запроса частичного изменения patch"):
        body = {"name": "НАИМЕНОВАНИЕ"}
        headers = {"Content-Type": "application/json"}
        response = requests.patch(
            f"{http_url_portal}/{create_and_delete_object}", json=body, headers=headers
        )
    with allure.step("Проверка статус кода ответа = 200"):
        assert response.status_code == 200, "Объект не изменен"
    with allure.step("Печатаем результат"):
        print(response.json())


@allure.feature("Posts")
@allure.story("Delete posts")
@pytest.mark.smoke
def test_delete(print_before_after_every_test, create_object):
    response = requests.delete(f"{http_url_portal}/{create_object}")
    with allure.step("Проверка статус кода ответа = 200"):
        assert response.status_code == 200, "Объект не удален"
