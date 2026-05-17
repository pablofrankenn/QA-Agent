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

def test_add_product_to_cart(page):
    page.goto(BASE_URL)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    
    page.click("[data-test='add-to-cart-sauce-labs-backpack']")
    
    cart_badge = page.locator(".shopping_cart_badge")
    expect(cart_badge).to_have_text("1")

def test_complete_checkout(page):
    page.goto(BASE_URL)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    
    page.click("[data-test='add-to-cart-sauce-labs-backpack']")
    page.click(".shopping_cart_link")
    
    expect(page).to_have_url(f"{BASE_URL}/cart.html")
    page.click("[data-test='checkout']")
    
    page.fill("[data-test='firstName']", "John")
    page.fill("[data-test='lastName']", "Doe")
    page.fill("[data-test='postalCode']", "12345")
    page.click("[data-test='continue']")
    
    page.click("[data-test='finish']")
    
    expect(page).to_have_url(f"{BASE_URL}/checkout-complete.html")
    expect(page.locator(".complete-header")).to_contain_text("Thank you")

def test_remove_product_from_cart(page):
    page.goto(BASE_URL)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    
    page.click("[data-test='add-to-cart-sauce-labs-backpack']")
    page.click(".shopping_cart_link")
    page.click("[data-test='remove-sauce-labs-backpack']")
    
    expect(page.locator(".cart_item")).to_have_count(0)

def test_sort_products(page):
    page.goto(BASE_URL)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    
    page.select_option("[data-test='product-sort-container']", "za")
    
    first_product = page.locator(".inventory_item_name").first
    expect(first_product).to_contain_text("Test.allTheThings()")