import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.DataTypes import DataTypes
from pages.Submit import Submit


@allure.epic("Главная страница")
@allure.severity("major")
@allure.story("проверка цветов выделения полей при заполнении")
@allure.feature("Fill")
@allure.title("Подсветка полей на странице в зависимости от корректного/некорректного заполнения")
@allure.description("заполнение формы обратной связи")
@allure.suite("Тест цветов")
def test_form():
    browser = webdriver.Chrome()
    with allure.step("Открыть страницу: https://bonigarcia.dev/selenium-webdriver-java/data-types.html"):
        datatypes = DataTypes(browser)


    with allure.step("Заполнить поля значениями:"):
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

    with allure.step("Нажать кнопку Submit"):
        submit = Submit(browser)

    with allure.step("выбор элемента подсвеченного красным для установки параметров красного цвета"):
        red = submit.zip_code().value_of_css_property("color")
    with allure.step("выбор элемента подсвеченного зеленым для установки параметров зеленого цвета"):
        green = submit.first_name().value_of_css_property("color")
    with allure.step("Проверить что поле Zip code подсвечено красным"):
        assert submit.zip_code().value_of_css_property("color") == red

    with allure.step("формирование списка заполненных полей"):
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

    with allure.step("Проверить, что заполненные елементы подсвечены зеленым цветом"):
        for element in elements:
            assert element.value_of_css_property("color") == green

    browser.quit()
