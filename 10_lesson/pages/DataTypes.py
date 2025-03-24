import allure
from selenium.webdriver.common.by import By


@allure.epic("Главная страница")
@allure.severity("major")
class DataTypes:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    @allure.step("Заполнение поля first name {data}")
    def first_name(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='first-name']").send_keys(data)

    @allure.step("Заполнение поля last name {data}")
    def last_name(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='last-name']").send_keys(data)

    @allure.step("Заполнение поля address {data}")
    def address(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='address']").send_keys(data)

    @allure.step("Заполнение поля email {data}")
    def email(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='e-mail']").send_keys(data)

    @allure.step("Заполнение поля phone_number {data}")
    def phone_number(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='phone']").send_keys(data)

    @allure.step("Заполнение поля zip_code {data}")
    def zip_code(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='zip-code']").send_keys(data)

    @allure.step("Заполнение поля city {data}")
    def city(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='city']").send_keys(data)

    @allure.step("Заполнение поля country {data}")
    def country(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='country']").send_keys(data)

    @allure.step("Заполнение поля job_position {data}")
    def job_position(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='job-position']").send_keys(data)

    @allure.step("Заполнение поля company {data}")
    def company(self, data):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='company']").send_keys(data)

    @allure.step("Нажать на кнопку Submit")
    def submit(self):
        self._driver.find_element(By.CSS_SELECTOR, "button.btn").click()
