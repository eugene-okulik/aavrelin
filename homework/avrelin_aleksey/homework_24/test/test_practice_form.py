import allure
import dotenv
import os

from endpoints.config_input_simple import ConfigPracticeForm
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


dotenv.load_dotenv()
BASE_URL_TEST2 = os.getenv("BASE_URL_TEST2")


@allure.feature("demoqa")
@allure.story("Страница Practice Form")
@allure.title("Успешное заполнение practice form")
def test_practice_form(driver):
    config = ConfigPracticeForm()

    with allure.step("Переход на главную страницу"):
        driver.get(BASE_URL_TEST2)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(("id", config.id_firstName)))

    with allure.step("Заполнение поля 'First Name'"):
        driver.find_element("id", config.id_firstName).send_keys(config.FirstName)

    with allure.step("Заполнение поля 'Last Name'"):
        driver.find_element("id", config.id_lastName).send_keys(config.LastName)

    with allure.step("Заполнение поля 'Email'"):
        driver.find_element("id", config.id_userEmail).send_keys(config.UserEmail)

    with allure.step("Заполнение поля 'Mobile Number'"):
        driver.find_element("id", config.id_mobile_number).send_keys(
            config.mobile_number
        )

    with allure.step("Нажать радиокнопку 'Male'"):
        driver.find_element("xpath", config.xpath_radiobutton_male).click()

    with allure.step("Открытие календаря"):
        calendar_input = driver.find_element("id", config.id_calendar)
        calendar_input.click()

    with allure.step("Выбор месяца 'April' в календаре"):
        month_dropdown = driver.find_element("class name", config.class_month)
        Select(month_dropdown).select_by_visible_text(config.month_name)

    with allure.step("Выбор года '2022' в календаре"):
        year_dropdown = driver.find_element("class name", config.class_year)
        Select(year_dropdown).select_by_visible_text(config.year)

    with allure.step("Выбор 15-го дня в календаре"):
        driver.find_element("class name", config.class_15_days).click()

    with allure.step("Заполнение поля 'Subjects'"):
        field = driver.find_element("xpath", config.xpath_subjects)
        field.send_keys(config.subjects)
        field.send_keys(Keys.ENTER)

    with allure.step("Выбор хобби 'Sports'"):
        driver.find_element("xpath", config.xpath_hobbies_sport).click()

    # with allure.step("Загрузка файла"):
    #     driver.find_element("id", config.id_uploadPicture).send_keys(config.upload_file)

    with allure.step("Заполнение поля 'Current Address'"):
        driver.find_element("id", config.id_current_address).send_keys(
            config.current_address
        )

    with allure.step("Выбор штата 'Haryana'"):
        driver.find_element("id", config.id_state).click()
        driver.find_element("id", config.id_state_haryana).click()

    with allure.step("Выбор города 'Panipat'"):
        driver.find_element("id", config.id_select_city).click()
        driver.find_element("id", config.id_city_panipat).click()

    with allure.step("Нажатие кнопки 'Submit'"):
        driver.find_element("id", config.id_button_submit).click()

    with allure.step("Проверяем назвиние таблицы в модальном окне"):
        wait = WebDriverWait(driver, 10)
        name_modal_header = wait.until(
            EC.visibility_of_element_located(("id", config.id_modal_header))
        ).text
        assert name_modal_header == config.name_modal_header
        print("\n", name_modal_header)

    entered_elements = {
        "Student Name": f"{config.FirstName} {config.LastName}",
        "Student Email": config.UserEmail,
        "Gender": config.gender,
        "Mobile": config.mobile_number,
        "Date of Birth": f"{config.day} {config.month_name},{config.year}",
        "Subjects": config.subjects,
        "Hobbies": config.hobbies,
        # "Picture": config.upload_file.split("\\")[-1],
        "Picture": "",
        "Address": config.current_address,
        "State and City": f"{config.State} {config.City}",
    }

    with allure.step("Проверяем каждую строку таблицы в модальном окне"):
        table_element = driver.find_elements("css selector", ".table tbody tr")
        for element in table_element:
            label = element.find_element("css selector", "td:first-child").text
            value = element.find_element("css selector", "td:last-child").text
            assert value == entered_elements[label]
            print(label, " - ", value)
