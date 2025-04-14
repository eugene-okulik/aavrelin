import json

from time import sleep
from playwright.sync_api import Page, Route, expect

# def test_change_response_iphone_16_pro(page: Page):
#     page.goto("https://www.apple.com/shop/buy-iphone", wait_until="domcontentloaded")
#     page.locator(".rf-hcard-content-title").nth(0).click()
#     popup = page.get_by_role("dialog")
#     expect(popup).to_be_visible()
#     title_iphone_16_pro = page.locator("h2.rf-digitalmat-overlay-header").nth(0)
#     expect(title_iphone_16_pro).to_have_text("iPhone 16 Pro")

def test_change_iphone_name_in_popup(page: Page):
    def change_response(route: Route):
        response = route.fetch()
        body = response.json()
        body["body"]["digitalMat"][0]["familyTypes"][0]["tabTitle"] = "яблокофон 16 про"
        body["body"]["digitalMat"][0]["familyTypes"][0]["productName"] = "яблокофон 16 про"
        route.fulfill(
            response=response,
            body=json.dumps(body)
        )
    page.route(
        "https://www.apple.com/shop/api/digital-mat?path=library/step0_iphone/digitalmat",
        change_response
    )
    page.goto("https://www.apple.com/shop/buy-iphone", wait_until="networkidle")
    page.locator(".rf-hcard-content-title").nth(0).click()
    sleep(3)
    popup = page.get_by_role("dialog")
    expect(popup).to_be_visible()
    expect(page.locator("#tab-\:r21\:-0")).to_have_text("яблокофон 16 про")
    expect(page.locator("#rf-digitalmat-overlay-label-0").nth(0)).to_have_text("яблокофон 16 про")
