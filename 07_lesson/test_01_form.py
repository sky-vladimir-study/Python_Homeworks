import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.DataTypes import DataTypes
from pages.Submit import Submit


def test_form():
    browser = webdriver.Chrome()
    datatypes = DataTypes(browser)

    datatypes.first_name("Иван")
    datatypes.last_name("Петров")
    datatypes.address("Ленина, 55-3")
    datatypes.email("test@skypro.com")
    datatypes.phone_number("+7985899998787")
    datatypes.zip_code("")
    datatypes.city("Москва")
    datatypes.country("Россия")
    datatypes.job_position("QA")
    datatypes.company("SkyPro")

    submit = Submit(browser)

    red = submit.zip_code().value_of_css_property("color")
    green = submit.first_name().value_of_css_property("color")
    assert submit.zip_code().value_of_css_property("color") == red

    elements = [
        submit.first_name(),
        submit.last_name(),
        submit.address(),
        submit.email(),
        submit.phone_number(),
        submit.city(),
        submit.country(),
        submit.job_position(),
        submit.company()
       ]

    for element in elements:
        assert element.value_of_css_property("color") == green

    browser.quit()
