from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.maximize_window()

    def set_delay(self, delay):
        delay_input = self._driver.find_element(By.CSS_SELECTOR, "input#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, button):
        self._driver.find_element(
            By.XPATH, f"//span[text()='{button}']").click()

    def wait_for_result(self, delay, result):
        WebDriverWait(self._driver, delay).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, ".screen"), result)
        )

    def final_result(self):
        result = self._driver.find_element(By.CSS_SELECTOR, ".screen").text
        return result
