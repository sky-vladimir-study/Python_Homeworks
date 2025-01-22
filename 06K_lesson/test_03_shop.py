import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Откройте сайт магазина
def test_shop():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    # Авторизуйтесь как пользователь
    username = driver.find_element(By.CSS_SELECTOR, "#user-name")
    username.clear()
    username.send_keys("standard_user")

    password = driver.find_element(By.CSS_SELECTOR, "#password")
    password.clear()
    password.send_keys("secret_sauce")

    driver.find_element(By.CSS_SELECTOR, '#login-button').click()
    # Добавьте в корзину товары
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
    # Перейдите в корзину
    driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()
    # Нажмите Checkout
    driver.find_element(By.CSS_SELECTOR, '#checkout').click()
    # заполнение формы
    first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
    first_name.clear()
    first_name.send_keys("Vladimir")

    last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
    last_name.clear()
    last_name.send_keys("Chirkov")

    postal_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    postal_code.clear()
    postal_code.send_keys("606000")
    # Нажмите кнопку Continue
    driver.find_element(By.CSS_SELECTOR, '#continue').click()

    # Прочитайте со страницы итоговую стоимость (Total)
    total = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
    print(total)
    # Проверьте, что итоговая сумма равна $58.29
    assert total == 'Total: $58.29'
    # закрыть браузер
    driver.quit()
