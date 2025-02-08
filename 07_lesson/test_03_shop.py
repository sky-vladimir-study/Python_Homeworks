from selenium import webdriver
from pages.AuthPage import AuthPage
from pages.CartPage import CartPage
from pages.InventoryPage import InventoryPage
from pages.UserInfoPage import UserInfoPage
from pages.SummaryPage import SummaryPage


def test_shop():
    browser = webdriver.Chrome()

    auth_page = AuthPage(browser)
    auth_page.authorization("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser)
    inventory_page.add_to_cart()

    cart_page = CartPage(browser)
    cart_page.go_to_cart()
    cart_page.checkout()

    user_page_info = UserInfoPage(browser)
    user_page_info.add_user_info("Vladimir", "Chirkov", "606000")

    summary_page = SummaryPage(browser)
    total_sum = summary_page.get_total_sum()

    assert total_sum == 'Total: $58.29'
