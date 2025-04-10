import re

from playwright.sync_api import Page, expect, BrowserContext, Dialog


def test_alert_check(page: Page):

    def accept_alert(alert: Dialog):
        print(alert.message)
        print(alert.type)
        alert.accept()

    page.on("dialog", accept_alert)
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.get_by_role('link', name='Click').click()
    result_text_page = page.locator(".result-text")
    expect(result_text_page).to_have_text("Ok")

def test_new_tab(page: Page, context: BrowserContext):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")
    button_click = page.get_by_role('link', name='Click')
    with context.expect_page() as new_page_event:
        button_click.click()
    new_page = new_page_event.value
    expect(new_page.locator(".result-text")).to_have_text("I am a new page in a new tab")
    expect(button_click).to_be_enabled()
    new_page.close()

def test_button_color_change(page: Page):
    page.goto("https://demoqa.com/dynamic-properties", wait_until="domcontentloaded")
    color_change_button = page.locator("#colorChange")
    expect(color_change_button).not_to_have_class(re.compile("text-danger"), timeout=6000)
    expect(color_change_button).to_have_class(re.compile("text-danger"), timeout=10000)
    expect(color_change_button).to_have_css("color", "rgb(220, 53, 69)")
    color_change_button.click()
    expect(color_change_button).to_be_visible()
