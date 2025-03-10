import allure
import dotenv
import os

from endpoints.config_input_simple import PageElements
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


dotenv.load_dotenv()
BASE_URL = os.getenv("BASE_URL_TEST3")
dynamical = PageElements()


@allure.feature("the-internet")
@allure.story("Тест кнопки")
@allure.title("Проверка работы кнопки 'Start'")
def test_dynamic_loading(driver):

    with allure.step("Открывает главную страницу"):
        driver.get(BASE_URL)

    with allure.step("Нажать кнопку 'Start'"):
        button = driver.find_element("xpath", dynamical.button_start)
        button.click()

    with allure.step("Ожидание на странице 'Hello World!'"):
        wait = WebDriverWait(driver, 10)
        text = dynamical.text_word
        wait.until(EC.visibility_of_element_located(("xpath", text)))

    with allure.step("Сравниваем отображаемый текст на странице с 'Hello World!'"):
        result = driver.find_element("xpath", text).text
        assert result == "Hello World!"
        print(result)
