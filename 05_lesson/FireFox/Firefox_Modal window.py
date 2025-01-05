from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get('http://the-internet.herokuapp.com/entry_ad')

sleep(2)

driver.find_element(By.CSS_SELECTOR, '.modal-footer').click()

sleep(2)

driver.quit()
