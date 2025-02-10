from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://uitestingplayground.com/textinput")
my_button = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
my_button.send_keys("SkyPro")
click_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
click_button.click()

print(click_button.text)

driver.quit()
