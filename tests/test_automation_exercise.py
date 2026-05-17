import pytest
from playwright.sync_api import sync_playwright, expect

BASE_URL = "https://automationexercise.com"

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_viewport_size({"width": 1280, "height": 720})
        yield page
        browser.close()

def test_homepage_loads(page):
    page.goto(BASE_URL, wait_until="domcontentloaded")
    expect(page).to_have_title("Automation Exercise")

def test_navigate_to_login(page):
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_text("Signup / Login").click()
    expect(page).to_have_url(f"{BASE_URL}/login")
    expect(page.locator(".login-form")).to_be_visible()
    expect(page.locator(".signup-form")).to_be_visible()

def test_search_product(page):
    page.goto(f"{BASE_URL}/products", wait_until="domcontentloaded")
    page.fill("#search_product", "dress")
    page.click("#submit_search")
    expect(page.locator(".features_items")).to_contain_text("dress", ignore_case=True)

def test_navigate_to_products(page):
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_text("Products").click()
    expect(page).to_have_url(f"{BASE_URL}/products")
    expect(page.locator(".productinfo").first).to_be_visible()

def test_navigate_to_cart(page):
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.locator("a[href='/view_cart']").first.click()
    expect(page).to_have_url(f"{BASE_URL}/view_cart")

def test_login_with_invalid_credentials(page):
    page.goto(f"{BASE_URL}/login", wait_until="domcontentloaded")
    page.fill("[data-qa='login-email']", "invalid@email.com")
    page.fill("[data-qa='login-password']", "wrongpassword")
    page.click("[data-qa='login-button']")
    expect(page.locator("p:has-text('Your email or password is incorrect!')")).to_be_visible()