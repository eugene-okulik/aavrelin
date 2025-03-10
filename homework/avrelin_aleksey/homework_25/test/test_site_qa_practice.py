import allure

from endpoints.config_input_simple import ConfQAPractice
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


config = ConfQAPractice()


@allure.feature("qa-practice")
@allure.story("Меню 'Inputs'")
class TestInputs:
    @allure.title("Успешное добавление текста во вкладке 'Text input'")
    def test_text_inputs(self, driver, base_url_practice):

        with allure.step("Выбрать вкладку меню Imputs"):
            driver.find_element("xpath", config.menu_inputs).click()

        with allure.step("Ввести текст"):
            text_in_field = driver.find_element("id", config.id_submits)
            text_in_field.send_keys(config.input_data)

        with allure.step("Нажать Enter"):
            text_in_field.send_keys(Keys.ENTER)

        with allure.step("Сравнить введенный текст с результатом"):
            result_text = driver.find_element("id", config.id_text_result)
            assert result_text.text == config.input_data

        with allure.step("Распечатать текст"):
            print('\n', result_text.text)

    @allure.title("Успешное добавление email во вкладке 'Email field'")
    def test_good_email_field(self, driver, base_url_practice):

        with allure.step("Выбрать вкладку меню Imputs"):
            driver.find_element("xpath", config.menu_inputs).click()

        with allure.step('Выбрать во вкладку "Email_field"'):
            driver.find_element("xpath", config.email_field).click()

        with allure.step("В поле ввести валидный email"):
            text_in_field = driver.find_element("id", config.id_email)
            text_in_field.send_keys(config.email_good)

        with allure.step("Нажать Enter"):
            text_in_field.send_keys(Keys.ENTER)

        with allure.step("Сравнить введенный текст с результатом"):
            result_text = driver.find_element("id", config.id_text_result)
            assert (
                result_text.text == config.email_good
            ), f"Результат не равен {config.email_good}"

    @allure.title("Ошибка при добавление невалидного email во вкладке 'Email field'")
    def test_bad_email_field(self, driver, base_url_practice):

        with allure.step("Выбрать вкладку меню Imputs"):
            driver.find_element("xpath", config.menu_inputs).click()

        with allure.step('Выбрать во вкладку "Email_field"'):
            driver.find_element("xpath", config.email_field).click()

        with allure.step("В поле ввести невалидный email"):
            text_in_field = driver.find_element("id", config.id_email)
            text_in_field.send_keys(config.email_bad)

        with allure.step("Нажать Enter"):
            text_in_field.send_keys(Keys.ENTER)

        with allure.step("Сравнить введенный текст с результатом"):
            result_text = driver.find_element("id", config.id_error_email)
            assert (
                result_text.text == config.email_error_text
            ), f"Результат не равен {config.email_error_text}"

    @allure.title("Успешное добавления пароля во вкладке 'Password field'")
    def test_good_password_field(self, driver, base_url_practice):

        with allure.step("Выбрать вкладку меню Imputs"):
            driver.find_element("xpath", config.menu_inputs).click()

        with allure.step('Выбрать во вкладку "Password field"'):
            driver.find_element("xpath", config.password_field).click()

        with allure.step("В поле ввести надежный пароль"):
            text_in_field = driver.find_element("id", config.id_password)
            text_in_field.send_keys(config.good_password)

        with allure.step("Нажать Enter"):
            text_in_field.send_keys(Keys.ENTER)

        with allure.step("Сравнить введенный текст с результатом"):
            result_text = driver.find_element("id", config.id_text_result)
            assert (
                result_text.text == config.good_password
            ), f"Результат не равен {config.good_password}"

    @allure.title("Добавление плохого пароля во вкладке 'Password field'")
    def test_bad_password_field(self, driver, base_url_practice):

        with allure.step("Выбрать вкладку меню Imputs"):
            driver.find_element("xpath", config.menu_inputs).click()

        with allure.step('Выбрать вкладку "Password field"'):
            driver.find_element("xpath", config.password_field).click()

        with allure.step("В поле ввести плохой пароль"):
            text_in_field = driver.find_element("id", config.id_password)
            text_in_field.send_keys(config.bad_password)

        with allure.step("Нажать Enter"):
            text_in_field.send_keys(Keys.ENTER)

        with allure.step("Проверить наличие плейсхолдера"):
            error_result_text = driver.find_element("id", config.id_error_password)
            assert (
                error_result_text.text == config.error_text_password
            ), f"Отсутствует {config.error_text_password}"


@allure.feature("qa-practice")
@allure.story("Меню 'Select'")
class TestSelect:
    @allure.title("Выбор языка програмирования")
    def test_practice_form(self, driver, base_url_practice):

        with allure.step("Выбрать вкладку меню Select"):
            driver.find_element("xpath", config.menu_select).click()

        with (allure.step("В поле выбирать селектор 'Java'")):
            dropdown = driver.find_element("id", config.id_choose_language)
            select_element = Select(dropdown)
            select_element.select_by_value("4")
            selected_text = select_element.first_selected_option.text

        with allure.step("Нажать кнопку 'Submit'"):
            driver.find_element("xpath", config.xpath_submits).click()

        with allure.step("Сравнить выбранный язык с результатом вывода"):
            result_text = driver.find_element(
                "class name", config.class_result_text
            ).text
            assert selected_text == result_text
