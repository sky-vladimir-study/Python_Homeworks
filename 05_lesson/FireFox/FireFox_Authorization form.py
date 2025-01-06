from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get('http://the-internet.herokuapp.com/login')

user = driver.find_element(By.CSS_SELECTOR, "#username")
pwd = driver.find_element(By.CSS_SELECTOR, "#password")

user.send_keys("tomsmith")
pwd.send_keys("SuperSecretPassword!")

driver.find_element(By.CSS_SELECTOR, '.radius').click()

sleep(2)

driver.quit()
