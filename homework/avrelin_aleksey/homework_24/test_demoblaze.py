import time

import allure
import pytest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    options = Options()
    # options.add_experimental_option("detach", True)
    # options.page_load_strategy = "eager"
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@allure.title("Добавление товара в корзину")
def test_add_products_in_cart(driver):

    with allure.step("Открыть ссылку"):
        driver.get("https://www.demoblaze.com/index.html")

    with allure.step("Открыть товар в новой вкладке браузера"):
        driver.implicitly_wait(5)
        nokia = driver.find_element("xpath", "(//h4[@class='card-title']/a)[2]")
        name_nokia = nokia.text
        action = ActionChains(driver)
        action.key_down(Keys.CONTROL).click(nokia).key_up(Keys.CONTROL).perform()

    with allure.step("Добавить товар в корзину"):
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        add_cart = driver.find_element(
            "xpath", "//div[@class='col-sm-12 col-md-6 col-lg-6']/a"
        )
        add_cart.click()
        # дожидаемся алерта, иначе тест падает
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = Alert(driver)
        alert.accept()

    with allure.step("Закрыть вкладку с товаром"):
        driver.close()
        driver.switch_to.window(tabs[0])
        time.sleep(5)
    with allure.step("На начальной вкладке открыть корзину"):
        cart = driver.find_element("xpath", "//li/a[@id='cartur']")
        cart.click()

    with allure.step("Проверить, что в корзине тот товар, который ранее добавили"):
        cart_product = driver.find_element("xpath", "//tr[@class='success']/td[2]").text
        assert cart_product == name_nokia
