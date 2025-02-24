import requests
import allure

from test_api_aavrelin.endpoints.base_endpoint import Endpoint


class CreatePost(Endpoint):

    @allure.step("Создание нового объекта")
    def create_new_post(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=body,
            headers=headers
        )
        if 'application/json' in self.response.headers.get('Content-Type', ''):
            try:
                self.json = self.response.json()
            except:
                raise ValueError("Сервер вернул не JSON")
        return self.response
