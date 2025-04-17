import allure
import pytest

from pages import data_for_test


@allure.feature("Создание аккаунта")
class TestCustomerRegistration:

    @allure.title("Успешная регистрация нового пользователя")
    def test_successful_account_creation(self, customer_page):
        # Открыть страницу
        customer_page.open_page()

        # Заполнить форму валидными данными
        password = "А2312!asd"
        customer_page.fill_customer_form_with_password(password)

        # Нажать кнопку 'Create an Account'
        customer_page.click_create_account_button()

        # Сравнить ожидаемый результат и фактический
        customer_page.verify_success_message(data_for_test.success_message)

    @allure.title("Попытка регистрации с некорректным паролем")
    @pytest.mark.parametrize("password", ["243234", "a", "ssss", "ADas!@d"])
    def test_registration_with_invalid_password(self, customer_page, password):
        # Открыть страницу
        customer_page.open_page()

        # Заполнить форму паролем меньше 8 символов
        customer_page.fill_customer_form_with_password(password)

        # Нажать кнопку 'Create an Account'
        customer_page.click_create_account_button()

        # Сравнить ожидаемый результат и фактический
        customer_page.verify_password_error_message(data_for_test.error_password_message)
