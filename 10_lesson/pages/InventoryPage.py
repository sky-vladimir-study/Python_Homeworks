import allure
from selenium.webdriver.common.by import By


class InventoryPage:

    def __init__(self, browser):
        self._driver = browser

    @allure.step("Добавление в корзину товаров Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie")
    def add_to_cart(self):
        self._driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
