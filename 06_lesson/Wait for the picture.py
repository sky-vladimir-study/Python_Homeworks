from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.maximize_window()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter = WebDriverWait(driver, 40)
waiter.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div#image-container.col-12.py-2 img#landscape"))
)

img = driver.find_element(By.CSS_SELECTOR, "#award")
print(img.get_dom_attribute("src"))

driver.quit()
