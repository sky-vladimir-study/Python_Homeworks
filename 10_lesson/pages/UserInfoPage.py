import allure
from selenium.webdriver.common.by import By


class UserInfoPage:

    def __init__(self, browser):
        self._driver = browser

    @allure.step("Добавление информации о пользователе")
    def add_user_info(self, first_name, last_name, post_code):
        with allure.step("Заполнение поля first-name {first_name}"):
            self._driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys(first_name)

        with allure.step("Заполнение поля last-name {last_name}"):
            self._driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys(last_name)

        with allure.step("Заполнение поля last-name {last_name}"):
            self._driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys(post_code)
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()
