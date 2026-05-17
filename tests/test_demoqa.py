import pytest
from playwright.sync_api import sync_playwright, expect

BASE_URL = "https://demoqa.com"

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_viewport_size({"width": 1280, "height": 720})
        yield page
        browser.close()

def test_fill_text_box_form(page):
    page.goto(f"{BASE_URL}/text-box")
    page.fill("#userName", "John Doe")
    page.fill("#userEmail", "john@example.com")
    page.fill("#currentAddress", "123 Main St, Buenos Aires")
    page.fill("#permanentAddress", "456 Oak Ave, Mendoza")
    page.click("#submit")
    expect(page.locator("#output")).to_be_visible()
    expect(page.locator("#name")).to_contain_text("John Doe")
    expect(page.locator("#email")).to_contain_text("john@example.com")


def test_radio_button(page):
    page.goto(f"{BASE_URL}/radio-button")
    page.click("label[for='yesRadio']")
    expect(page.locator(".text-success")).to_contain_text("Yes")

def test_web_tables(page):
    page.goto(f"{BASE_URL}/webtables", wait_until="domcontentloaded")
    page.wait_for_timeout(2000)
    page.click("#addNewRecordButton")
    page.wait_for_timeout(500)
    page.fill("#firstName", "Pablo")
    page.fill("#lastName", "Test")
    page.fill("#userEmail", "pablo@test.com")
    page.fill("#age", "30")
    page.fill("#salary", "5000")
    page.fill("#department", "QA")
    page.click("#submit")
    page.wait_for_timeout(2000)
    expect(page.locator("table tbody")).to_contain_text("Pablo")

def test_buttons_interaction(page):
    page.goto(f"{BASE_URL}/buttons")
    page.dblclick("#doubleClickBtn")
    expect(page.locator("#doubleClickMessage")).to_contain_text("You have done a double click")
    page.click("#rightClickBtn", button="right")
    expect(page.locator("#rightClickMessage")).to_contain_text("You have done a right click")