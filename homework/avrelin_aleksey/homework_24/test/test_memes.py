import allure
from endpoints.base_endpoint import memes_data


@allure.feature("Мемы")
class TestMemes:
    @allure.story("Создание мема")
    def test_create_memes(self, memes_endpoint, token):
        response = memes_endpoint.create_memes(token, **memes_data)
        memes_endpoint.check_status_code(200)
        assert response["id"] is not None

    @allure.story("Получение мема по id")
    def test_get_memes_by_id(self, memes_endpoint, token, create_memes_for_test):
        response = memes_endpoint.get_memes_by_id(create_memes_for_test, token)
        memes_endpoint.check_status_code(200)
        assert response["id"] == create_memes_for_test

    @allure.story("Изменение мема")
    def test_update_memes(self, memes_endpoint, token, create_memes_for_test):
        updated_data = {
            "id": create_memes_for_test,
            "text": "Updated Meme",
            "url": "https://alekseys.mem/updated_memes.jpg",
            "tags": ["updated", "test2"],
            "info": {"key": "updated_value"},
        }
        response = memes_endpoint.update_memes(
            create_memes_for_test, token, **updated_data
        )
        memes_endpoint.check_status_code(200)
        assert response["text"] == "Updated Meme"

    @allure.story("Удаление мема")
    def test_delete_memes(self, memes_endpoint, token, create_memes_for_test):
        response = memes_endpoint.delete_memes(create_memes_for_test, token)
        memes_endpoint.check_status_code(200)
