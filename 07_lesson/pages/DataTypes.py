from selenium.webdriver.common.by import By


class DataTypes:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def first_name(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='first-name']").send_keys(data)

    def last_name(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='last-name']").send_keys(data)

    def address(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='address']").send_keys(data)

    def email(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='e-mail']").send_keys(data)

    def phone_number(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='phone']").send_keys(data)

    def zip_code(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='zip-code']").send_keys(data)

    def city(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='city']").send_keys(data)

    def country(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='country']").send_keys(data)

    def job_position(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='job-position']").send_keys(data)

    def company(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='company']").send_keys(data)

    def submit(self):
        self._driver.find_element(By.CSS_SELECTOR, "button.btn").click()
