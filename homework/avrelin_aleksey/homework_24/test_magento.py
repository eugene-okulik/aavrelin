import allure
import pytest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
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


@allure.title("Проверка появления товара")
def test_add_products_compare_list(driver):

    with allure.step("Открыть ссылку"):
        driver.get("https://magento.softwaretestingboard.com/gear/bags.html")

    with allure.step("Навести курсор на первый товар"):
        first_product = driver.find_element(
            "xpath", "//li[@class='item product product-item'][1]"
        )
        name_first_product = first_product.text.split("\n")[0]
        ActionChains(driver).move_to_element(first_product).perform()

    with allure.step("Кликнуть внизу карточки товара на кнопку Add to compare"):
        button_add_to_compare = driver.find_element(
            "xpath", "//div/a[@class='action tocompare']"
        )
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of(button_add_to_compare))
        button_add_to_compare.click()

    with allure.step("Проверить, что товар появился слева на этой же странице"):
        name = "//strong[@class='product-item-name']/a"
        compare_list = wait.until(EC.visibility_of_element_located(("xpath", name)))
        assert compare_list.is_displayed()

    with allure.step("Проверитть название товара в сравнении"):
        compare_list_name = driver.find_element("xpath", name)
        assert name_first_product == compare_list_name.text
        # print('\n',compare_list_name.text)
