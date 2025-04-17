from playwright.sync_api import Page, Locator
import allure


class BasePage:
    base_url = "https://magento.softwaretestingboard.com"
    page_url = None

    def __init__(self, page: Page):
        self.page = page


    def open_page(self):
        with allure.step(f"Открываем страницу"):
            if self.page_url:
                self.page.goto(f"{self.base_url}{self.page_url}", wait_until='domcontentloaded')
            else:
                raise NotImplementedError("Страница не может быть открыта")

    def find(self, locator) -> Locator:
        return self.page.locator(locator)
