import requests
import allure

from test_api_aavrelin.endpoints.base_endpoint import Endpoint


class DeletePost(Endpoint):
    @allure.step("Удаление объекта")
    def delete_post(self, post_id):
        self.response = requests.delete(f"{self.url}/{post_id}")
        return self.response
