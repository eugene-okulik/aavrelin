import allure
import pytest

from test_api_aavrelin.endpoints.data_for_test import TEST_DATA_1
from test_api_aavrelin.endpoints.data_for_test import NEGATIVE_DATA




@pytest.mark.smoke
@allure.title("Успешное создание объекта")
@pytest.mark.parametrize("body", TEST_DATA_1)
def test_create_post(check_post_test_status_code, create_post_endpoint, body):
    create_post_endpoint.create_new_post(body)
    check_post_test_status_code.check_status_code(200)


@pytest.mark.smoke
@allure.title("Создание объекта с невалидным body")
@pytest.mark.parametrize("body", NEGATIVE_DATA)
def test_post_with_negative_object(check_post_test_status_code, create_post_endpoint, body):
    create_post_endpoint.create_new_post(body)
    check_post_test_status_code.check_bad_status_code()
