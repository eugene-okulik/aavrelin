import allure
import pytest

from test_api_aavrelin.endpoints.data_for_test import TEST_DATA_2


@allure.title("Успешное иполное изменение объекта")
@pytest.mark.parametrize("body", TEST_DATA_2)
@pytest.mark.smoke
def test_update_put_post(check_update_test_status_code, update_post_endpoint, create_and_delete_object, body):
    update_post_endpoint.update_put_post(create_and_delete_object, body)
    check_update_test_status_code.check_status_code(200)


@allure.title("Успешное частичное изменение объекта")
@pytest.mark.smoke
@pytest.mark.critical
@pytest.mark.parametrize("body", TEST_DATA_2)
def test_update_patch_post(check_update_test_status_code, update_post_endpoint, create_and_delete_object, body):
    update_post_endpoint.update_patch_post(create_and_delete_object, body)
    check_update_test_status_code.check_status_code(200)
