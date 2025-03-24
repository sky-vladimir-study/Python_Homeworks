import allure
from selenium.webdriver.common.by import By


class AuthPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.maximize_window()

    @allure.step("Авторизация по логину {username} и паролю {password}")
    def authorization(self, username, password):
        self._driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys(username)
        self._driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()
