import requests
import allure

from test_api_aavrelin.endpoints.base_endpoint import Endpoint


class UpdatePost(Endpoint):

    @allure.step("Изменение объекта c помощью put")
    def update_put_post(self, post_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f"{self.url}/{post_id}",
            json=body,
            headers=headers
        )
        return self.response

    @allure.step("Изменение объекта c помощью patch")
    def update_patch_post(self, post_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f"{self.url}/{post_id}",
            json=body,
            headers=headers
        )
        return self.response
