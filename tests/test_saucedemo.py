import pytest
from playwright.sync_api import sync_playwright, expect

BASE_URL = "https://www.saucedemo.com"

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()

def test_successful_login(page):
    page.goto(BASE_URL)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    expect(page).to_have_url(f"{BASE_URL}/inventory.html")

def test_locked_out_user(page):
    page.goto(BASE_URL)
    page.fill("#user-name", "locked_out_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    expect(page.locator("[data-test='error']")).to_be_visible()
    expect(page.locator("[data-test='error']")).to_contain_text("locked out")

def test_incorrect_password(page):
    page.goto(BASE_URL)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "wrong_password")
    page.click("#login-button")
    expect(page.locator("[data-test='error']")).to_be_visible()
    expect(page.locator("[data-test='error']")).to_contain_text("do not match")

def test_problem_user_login(page):
    page.goto(BASE_URL)
    page.fill("#user-name", "problem_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    expect(page).to_have_url(f"{BASE_URL}/inventory.html")

def test_performance_glitch_user(page):
    page.goto(BASE_URL)
    page.fill("#user-name", "performance_glitch_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    expect(page).to_have_url(f"{BASE_URL}/inventory.html", timeout=10000)