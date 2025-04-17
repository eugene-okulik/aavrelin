import allure
from pages import data_for_test

@allure.feature("Работа с коллекциями товаров")
class TestProductCollections:

    def _prepare_collection_page(self, collection_page):
        # Открыть страницу
        collection_page.open_page()
        # Выбор в меню STYLE(Tee) - SIZE(XL) - CLIMATE(Indoor) - COLOR(blue)
        collection_page.apply_product_filters(data_for_test.filters)
        return collection_page

    @allure.title("Применение фильтров к коллекции товаров")
    def test_apply_product_filters(self, collection_page):
        self._prepare_collection_page(collection_page)
        # Проверить список всех добавленных фильтров
        collection_page.verify_applied_filters(data_for_test.filters)

    @allure.title("Добавление товаров в сравнение")
    def test_add_products_to_compare(self, collection_page):
        self._prepare_collection_page(collection_page)
        # Поменять цвет первого товара на белый
        collection_page.change_first_tee_color_to_white()

        # Добавить первый товар в сравнение
        collection_page.add_product_to_compare(1)

        # Добавить второй товар в сравнение
        collection_page.add_product_to_compare(2)

        # Нажать кнопку сравнения в уведомлении
        collection_page.click_compare_button_in_notification()

        # Проверка что на странице есть два добавленных в сравнение товара
        collection_page.verify_compare_list_has_products(2)
