import pytest
import random

from playwright.sync_api import Page, BrowserContext
from pages.collections import CollectionPage
from pages.customer import CustomerPage
from pages.sale import SalePage


@pytest.fixture()
def page(context: BrowserContext):
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    yield page
    page.screenshot(path=f"{str(random.randint(100,10000))}_screenshot.png")


@pytest.fixture()
def customer_page(page: Page):
    return CustomerPage(page)


@pytest.fixture()
def collection_page(page: Page):
    return CollectionPage(page)


@pytest.fixture()
def sale_page(page: Page):
    return SalePage(page)
