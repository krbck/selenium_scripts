from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


username = "root"
password = "1234567890pX"

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--incognito")
chromeOptions.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chromeOptions)

driver.get("https://192.168.1.155:8006/")
driver.find_element(By.CSS_SELECTOR, '[id="textfield-1066-inputEl"]').send_keys(username)
driver.find_element(By.CSS_SELECTOR, '[id="textfield-1067-inputEl"]').send_keys(password)
driver.find_element(By.CSS_SELECTOR, '[id="button-1071-btnInnerEl"]').click()
wait = WebDriverWait(driver, 20)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id="button-1005-btnEl"]'))).click()
sleep(300)