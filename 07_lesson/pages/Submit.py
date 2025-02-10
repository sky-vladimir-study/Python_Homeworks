from selenium.webdriver.common.by import By


class Submit:

    def __init__(self, browser):
        self.driver = browser
        submit_button = self.driver.find_element(
            By.CSS_SELECTOR, "button.btn")
        submit_button.click()

    def first_name(self):
        first_name = self.driver.find_element(
            By.CSS_SELECTOR, "#first-name")
        return first_name

    def last_name(self):
        last_name = self.driver.find_element(
            By.CSS_SELECTOR, "#last-name")
        return last_name

    def address(self):
        address = self.driver.find_element(
            By.CSS_SELECTOR, "#address")
        return address

    def email(self):
        email = self.driver.find_element(
            By.CSS_SELECTOR, "#e-mail")
        return email

    def phone_number(self):
        phone_number = self.driver.find_element(
            By.CSS_SELECTOR, "#phone")
        return phone_number

    def zip_code(self):
        zip_code = self.driver.find_element(
            By.CSS_SELECTOR, "#zip-code")
        return zip_code

    def city(self):
        city = self.driver.find_element(
            By.CSS_SELECTOR, "#city")
        return city

    def country(self):
        country = self.driver.find_element(
            By.CSS_SELECTOR, "#country")
        return country

    def job_position(self):
        job_position = self.driver.find_element(
            By.CSS_SELECTOR, "#job-position")
        return job_position

    def company(self):
        company = self.driver.find_element(
            By.CSS_SELECTOR, "#company")

        return company
