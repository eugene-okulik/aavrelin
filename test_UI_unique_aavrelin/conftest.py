import pytest

from playwright.sync_api import Page
from pages.collections import CollectionPage
from pages.customer import CustomerPage
from pages.sale import SalePage


@pytest.fixture()
def customer_page(page: Page):
    return CustomerPage(page)

@pytest.fixture()
def collection_page(page: Page):
    return CollectionPage(page)

@pytest.fixture()
def sale_page(page: Page):
    return SalePage(page)
