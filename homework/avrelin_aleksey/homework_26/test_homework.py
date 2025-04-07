import re
import allure

from playwright.sync_api import Page, expect


def test_form_authentication(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Form Authentication").click()
    field_login = page.get_by_role("textbox", name="Username")
    field_login.fill("aleksey")
    field_passw = page.get_by_role("textbox", name="Password")
    field_passw.fill("12345")
    page.get_by_role("button", name=" Login").click()


@allure.suite("Practice Form")
@allure.title("Заполнение формы")
def test_practice_form(page: Page):
    with allure.step("Открытие страницы"):
        page.goto(
            "https://demoqa.com/automation-practice-form", wait_until="domcontentloaded"
        )

    with allure.step("Проверка заголовка страницы"):
        expect(page).to_have_title(re.compile("DEMOQA"))

    with allure.step("Заполнение имени"):
        first_name_field = page.get_by_placeholder("First Name")
        first_name_field.fill("Алексей")
        last_name_field = page.get_by_placeholder("Last Name")
        last_name_field.fill("Романов")

    with allure.step("Заполнение email"):
        email_field = page.get_by_placeholder("name@example.com")
        email_field.fill("alexey@lesson.ru")

    with allure.step("Выбор пола"):
        male_radio = page.locator("label[for='gender-radio-1']")
        male_radio.check()

    with allure.step("Заполнение номера телефона"):
        mobile_field = page.get_by_placeholder("Mobile Number")
        mobile_field.fill("89776868586")

    with allure.step("Проверка даты рождения"):
        date_input = page.locator("#dateOfBirthInput")
        date_input.fill("08 Apr 2025")
        date_input.press("Enter")

    with (allure.step("Выбор предметов")):
        subjects_input = page.locator("#subjectsInput")
        subjects_input.click()
        subjects_input.fill("Maths")
        page.wait_for_timeout(100)
        subjects_input.press("Enter")
        page.wait_for_timeout(100)
        subjects_input.click()
        subjects_input.fill("Chemistry")
        page.wait_for_timeout(100)
        subjects_input.press("Enter")

    with allure.step("Выбор хобби"):
        hobbies_sports = page.locator("label[for='hobbies-checkbox-3']")
        hobbies_sports.check()

    with allure.step("Ввести адрес"):
        address_field = page.get_by_placeholder("Current Address")
        address_field.fill("Москва ул. Профсоюзная д.86")

    with allure.step("Выбор штата"):
        state_dropdown = page.locator("#state")
        state_dropdown.click()
        page.get_by_text("Haryana").click()

    with allure.step("Выбор города"):
        city_dropdown = page.locator("#city")
        city_dropdown.click()
        page.get_by_text("Panipat").click()

    with allure.step("Нажать Submit"):
        submit_button = page.get_by_role("button", name="Submit")
        submit_button.click()
