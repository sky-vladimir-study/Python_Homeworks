import allure
from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, browser):
        self._driver = browser

    @allure.step("Зайти в Корзину")
    def go_to_cart(self):
        self._driver.find_element(
            By.CSS_SELECTOR, 'a.shopping_cart_link').click()

    @allure.step("Нажать кнопку Checkout")
    def checkout(self):
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()
