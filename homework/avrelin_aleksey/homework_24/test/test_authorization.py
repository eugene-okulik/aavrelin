import allure


@allure.feature("Авторизация")
class TestAuthorization:
    @allure.story("Авторизация пользователя")
    def test_authorization_user(self, token):
        assert token is not None
