import allure
import requests
from endpoints.base_endpoint import BaseEndpoint


class Memes(BaseEndpoint):
    @allure.step("Получение списка мемов")
    def get_all_memes(self, token):
        self.headers["Authorization"] = token
        self.response = requests.get(f"{self.url}/meme", headers=self.headers)
        return self.response.json()

    @allure.step("Получение мема по ID")
    def get_memes_by_id(self, meme_id, token):
        self.headers["Authorization"] = token
        self.response = requests.get(f"{self.url}/meme/{meme_id}", headers=self.headers)
        return self.response.json()

    @allure.step("Создание мема")
    def create_memes(self, token, **meme_data):
        self.headers["Authorization"] = token
        self.response = requests.post(
            f"{self.url}/meme", json=meme_data, headers=self.headers
        )
        return self.response.json()

    @allure.step("Изменение мема")
    def update_memes(self, meme_id, token, **updated_data):
        self.headers["Authorization"] = token
        self.response = requests.put(
            f"{self.url}/meme/{meme_id}", json=updated_data, headers=self.headers
        )
        return self.response.json()

    @allure.step("Удаление мема")
    def delete_memes(self, meme_id, token):
        self.headers["Authorization"] = token
        self.response = requests.delete(
            f"{self.url}/meme/{meme_id}", headers=self.headers
        )
        return self.response
