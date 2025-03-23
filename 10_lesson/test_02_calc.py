import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.CalcPage import CalcPage


@allure.epic("Калькулятор")
@allure.severity("major")
@allure.story("тестирование работы калькулятора")
@allure.title("Проверка результата вычислений в соответствии с заданными параметрами")
@allure.description("вычисления калькулятора с ожиданием")
@allure.suite("Тест калькулятора")
def test_calc():
    browser = webdriver.Chrome()

    with allure.step("Открыть страницу https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"):
        calc_page = CalcPage(browser)

    calc_page.set_delay(45)

    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    calc_page.wait_for_result(46, "15")
    result = calc_page.final_result()

    with allure.step("Проверка, что полученный результат равен {result})"):
        assert int(result) == 15

    browser.quit()
