import allure
from selenium.webdriver.common.by import By


class SummaryPage:

    def __init__(self, browser):
        self._driver = browser

    @allure.step("Получение общей суммы заказа")
    def get_total_sum(self):
        total = self._driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text
        return total
