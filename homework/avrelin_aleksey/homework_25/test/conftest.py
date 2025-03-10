import pytest
import dotenv
import os
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from endpoints.config_input_simple import ConfQAPractice


config = ConfQAPractice()
dotenv.load_dotenv()
BASE_URL = os.getenv("BASE_URL_TEST1")


@pytest.fixture()
def driver():
    options = Options()
    options.add_experimental_option("detach", True)
    options.page_load_strategy = "eager"
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def base_url_practice(driver):
    with allure.step("Открыть главную страницу"):
        driver.get(BASE_URL)
        driver.find_element("xpath", config.menu_single_elements).click()
        driver.implicitly_wait(10)
