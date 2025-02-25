import allure
import pytest


@pytest.mark.smoke
@allure.title("Получение информации по объектам")
def test_get_post(check_get_test_status_code, get_post_endpoint, create_and_delete_object):
    get_post_endpoint.get_post(create_and_delete_object)
    check_get_test_status_code.check_status_code(200)
