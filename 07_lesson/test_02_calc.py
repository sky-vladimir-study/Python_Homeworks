from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.CalcPage import CalcPage


def test_calc():
    browser = webdriver.Chrome()

    calc_page = CalcPage(browser)
    calc_page.set_delay(45)

    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    calc_page.wait_for_result(46, "15")
    result = calc_page.final_result()

    assert int(result) == 15

    browser.quit()
