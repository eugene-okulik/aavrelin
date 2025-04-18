import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import sale_locator as loc


class SalePage(BasePage):
    page_url = "/sale.html"

    @allure.step("Проверка заголовка страницы")
    def verify_page_title(self, expected_title):
        page_title = self.find(loc.page_title_loc)
        expect(page_title).to_have_text(expected_title)

    def assert_promo_blocks_match_expected(self, expected_data):
        promo_blocks = self.page.locator(".block-promo").all()
        print(f"Найдено ссылок с акциями: {len(promo_blocks)}")

        with allure.step("Проверка количество ссылок"):
            assert len(promo_blocks) == len(expected_data), (
                f"Количество ссылок не совпадает: "
                f"{len(promo_blocks)} != {len(expected_data)}"
            )

        i = 0
        for block in promo_blocks:
            i += 1
            print(f"\nПроверка ссылки № = {i}:")

            with allure.step(f"Проверка ссылки {i}"):
                title_locator = block.locator(".title")
                title = title_locator.inner_text()
                print(f"Заголовок ссылки: {title}")
                expect(title_locator).to_have_text(expected_data[i - 1]["title"])

                info_locator = block.locator(".info")
                info = info_locator.inner_text()
                print(f"Информация: {info}")
                expect(info_locator).to_have_text(expected_data[i - 1]["info"])

                if expected_data[i - 1]["more"]:
                    more_locator = block.locator(".more")
                    more = more_locator.inner_text()
                    print(f"Текст кнопки: {more}")
                    expect(more_locator).to_have_text(expected_data[i - 1]["more"])
