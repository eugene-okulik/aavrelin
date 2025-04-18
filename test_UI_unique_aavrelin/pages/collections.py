import allure

from playwright.sync_api import expect
from pages.locators import collections_locator as loc
from pages.base_page import BasePage


class CollectionPage(BasePage):
    page_url = "/collections/eco-friendly.html"

    def apply_product_filters(self, filters):
        self.select_filter("style", filters["style"])
        self.select_filter("size", filters["size"])
        self.select_filter("climate", filters["climate"])
        self.select_filter("color", filters["color"])

    def select_filter(self, filter_type, value):
        filter_locators = {
            "style": (loc.menu_loc, loc.style_menu_tee_loc),
            "size": (loc.menu_loc, loc.size_menu_XL_loc),
            "climate": (loc.menu_loc, loc.climate_menu_indoor_loc),
            "color": (loc.menu_loc, loc.color_menu_blue_loc)
        }

        with allure.step(f"Применение фильтра {filter_type}: {value}"):
            menu_loc, value_loc = filter_locators[filter_type]
            if filter_type == 'style':
                self.find(menu_loc).nth(1).click()
            else:
                self.find(menu_loc).nth(0).click()
            value_locator = self.find(value_loc)
            expect(value_locator).to_be_visible(timeout=1000)
            value_locator.click()
            self.page.wait_for_timeout(2000)

    def verify_applied_filters(self, expected_filters):
        with allure.step("Проверка применённых фильтров"):
            filter_items = self.find(loc.filter_current_items_loc)
            expect(filter_items).to_have_count(len(expected_filters)), "Количество фильтров не совпадает"

            for i, (filter_name, expected_value) in enumerate(expected_filters.items()):
                label_locator = filter_items.nth(i).locator(loc.filter_label_loc)
                value_locator = filter_items.nth(i).locator(loc.filter_value_loc)

                expect(label_locator).to_have_text(filter_name.capitalize())
                expect(value_locator).to_have_text(expected_value)

    def change_first_tee_color_to_white(self):
        with allure.step("Изменение цвета первого товара на белый"):
            self.find(loc.color_tee_first_wight_loc).click()

    def add_product_to_compare(self, product_number):
        product_locator = (f"(//div[@class='product details product-item-details'])[{product_number}]")
        compare_locator = (f"(//div/a[@class='action tocompare'])[{product_number}]")

        with allure.step(f"Добавление товара #{product_number} в сравнение"):
            self.page.hover(product_locator)
            self.page.click(compare_locator)

    def click_compare_button_in_notification(self):
        with allure.step("Нажатие кнопки сравнения в уведомлении"):
            self.find(loc.button_comparison_list_loc).click()

    def verify_compare_list_has_products(self, expected_count):
        with allure.step(f"Проверка что в сравнении {expected_count} товара(ов)"):
            product_items = self.find(loc.product_items_loc)
            print(product_items)
            expect(product_items).to_have_count(expected_count)
