import allure


class StatusCode:

    def __init__(self, create_post_endpoint):
        self.create_post_endpoint = create_post_endpoint

    @allure.step("Проверка статус-кода")
    def check_status_code(self, expected_code):
        print(self.create_post_endpoint.response.status_code)
        assert self.create_post_endpoint.response.status_code == expected_code, \
            f'{expected_code} is not {expected_code}'

    @allure.step("Проверка статус-кода 400 при невалидном запросе")
    def check_bad_status_code(self):
        self.check_status_code(400)
