import requests
import allure

from test_api_aavrelin.endpoints.base_endpoint import Endpoint


class GetPost(Endpoint):
    @allure.step("Получение объекта")
    def get_post(self, post_id):
        self.response = requests.get(f"{self.url}/{post_id}")
        return self.response
