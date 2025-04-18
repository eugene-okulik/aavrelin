import allure

from pages import data_for_test


@allure.feature("Страница SALE")
class TestAccountCreation:
    @allure.title("Проверка ссылок на странице SALE")
    def test_checking_links_on_sale_page(self, sale_page):
        sale_page.open_page()
        sale_page.verify_page_title(data_for_test.expected_page)
        sale_page.assert_promo_blocks_match_expected(data_for_test.expected_promo)
