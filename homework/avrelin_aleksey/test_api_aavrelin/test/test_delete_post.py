import pytest
import allure


@pytest.mark.smoke
@allure.title("Удаление объекта")
def test_delete_post(check_delete_test_status_code, delete_post_endpoint, create_object):
    delete_post_endpoint.delete_post(create_object)
    check_delete_test_status_code.check_status_code(200)
