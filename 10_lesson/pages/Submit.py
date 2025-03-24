import allure
from selenium.webdriver.common.by import By


class Submit:

    def __init__(self, browser):
        self.driver = browser
        submit_button = self.driver.find_element(
            By.CSS_SELECTOR, "button.btn")
        submit_button.click()

    @allure.step("выбор элемента first name для возврата параметров цвета")
    def first_name(self):
        first_name = self.driver.find_element(
            By.CSS_SELECTOR, "#first-name")
        return first_name

    @allure.step("выбор элемента last_name для возврата параметров цвета")
    def last_name(self):
        last_name = self.driver.find_element(
            By.CSS_SELECTOR, "#last-name")
        return last_name

    @allure.step("выбор элемента address для возврата параметров цвета")
    def address(self):
        address = self.driver.find_element(
            By.CSS_SELECTOR, "#address")
        return address

    @allure.step("выбор элемента email для возврата параметров цвета")
    def email(self):
        email = self.driver.find_element(
            By.CSS_SELECTOR, "#e-mail")
        return email

    @allure.step("выбор элемента phone_number для возврата параметров цвета")
    def phone_number(self):
        phone_number = self.driver.find_element(
            By.CSS_SELECTOR, "#phone")
        return phone_number

    @allure.step("выбор элемента zip_code для возврата параметров цвета")
    def zip_code(self):
        zip_code = self.driver.find_element(
            By.CSS_SELECTOR, "#zip-code")
        return zip_code

    @allure.step("выбор элемента city для возврата параметров цвета")
    def city(self):
        city = self.driver.find_element(
            By.CSS_SELECTOR, "#city")
        return city

    @allure.step("выбор элемента country для возврата параметров цвета")
    def country(self):
        country = self.driver.find_element(
            By.CSS_SELECTOR, "#country")
        return country

    @allure.step("выбор элемента job_position для возврата параметров цвета")
    def job_position(self):
        job_position = self.driver.find_element(
            By.CSS_SELECTOR, "#job-position")
        return job_position

    @allure.step("выбор элемента company для возврата параметров цвета")
    def company(self):
        company = self.driver.find_element(
            By.CSS_SELECTOR, "#company")
        return company
