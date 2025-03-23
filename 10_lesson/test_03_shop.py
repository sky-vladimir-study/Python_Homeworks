import allure
from selenium import webdriver
from pages.AuthPage import AuthPage
from pages.CartPage import CartPage
from pages.InventoryPage import InventoryPage
from pages.UserInfoPage import UserInfoPage
from pages.SummaryPage import SummaryPage


@allure.epic("Интернет магазин")
@allure.severity("Major")
@allure.story("Тестирование корзины")
@allure.title("Проверка расчета общей суммы товаров в корзине")
@allure.description("Оформление заказа")
@allure.suite("Тест интернет магазина")
def test_shop():
    browser = webdriver.Chrome()

    with allure.step("Открыть сайт магазина: https://www.saucedemo.com/"):
        auth_page = AuthPage(browser)

    auth_page.authorization("standard_user", "secret_sauce")

    with allure.step("Выбрать товар"):
        inventory_page = InventoryPage(browser)

    inventory_page.add_to_cart()

    with allure.step("Нажать на корзину"):
        cart_page = CartPage(browser)

    cart_page.go_to_cart()
    cart_page.checkout()

    with allure.step("Страница информации о пользователе"):
        user_page_info = UserInfoPage(browser)

    user_page_info.add_user_info("Vladimir", "Chirkov", "606000")

    with allure.step("Расчет суммы"):
        summary_page = SummaryPage(browser)

    total_sum = summary_page.get_total_sum()

    with allure.step("Проверяем, что сумма = $58.29"):
        assert total_sum == 'Total: $58.29'
