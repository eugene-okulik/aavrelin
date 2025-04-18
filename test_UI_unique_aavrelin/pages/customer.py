import allure

from playwright.sync_api import expect
from pages.locators import customer_locator as loc
from pages.base_page import BasePage
from pages import data_for_test


class CustomerPage(BasePage):
    page_url = "/customer/account/create/"

    def fill_customer_form_with_password(self, password):
        with allure.step("Заполнение полей формы"):
            test_data = {
                "first_name": data_for_test.first_name,
                "last_name": data_for_test.last_name,
                "email": data_for_test.email,
                "password": password
            }
            self.fill_customer_form(test_data)

    def fill_customer_form(self, form_data):
        with allure.step("Заполнение формы регистрации"):
            self.page.wait_for_timeout(2000)
            self.find(loc.first_name_field_loc).fill(form_data["first_name"])
            self.find(loc.last_name_field_loc).fill(form_data["last_name"])
            self.find(loc.email_field_loc).fill(form_data["email"])
            self.find(loc.password_field_loc).fill(form_data["password"])
            self.find(loc.password_confirmation_loc).fill(form_data["password"])

    def click_create_account_button(self):
        with allure.step("Нажать кнопку 'Create an Account'"):
            self.find(loc.button_create_an_account).click()

    def verify_success_message(self, expected_text):
        self.assert_result("success_message", expected_text)

    def verify_password_error_message(self, expected_text):
        self.assert_result("password_error", expected_text)

    def assert_result(self, field_name, expected_text):
        locators = {
            "success_message": loc.success_message_loc,
            "password_error": loc.error_message_password_8symbols_loc
        }

        with allure.step(f"Сравнение полученного результата '{field_name}' с ожидаемым"):
            result_text = self.find(locators[field_name])
            expect(result_text).to_have_text(expected_text)
