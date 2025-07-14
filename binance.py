from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--user-data-dir=/home/burak/.config/google-chrome-selenium")  # Create a new profile directory for specific selenium use
options.add_argument("--profile-directory=Default") 
options.add_argument("--disable-extensions") # For performance improvement
options.add_argument("--no-first-run")
options.add_argument("--no-default-browser-check")
options.add_argument("--window-size=1920,1080") 
driver = webdriver.Chrome(options=options) 
driver.get("https://google.com")








while True:
    command = input("Type 'q' to quit and close browser: ")
    if command.lower() == 'q':
            break

driver.quit() 