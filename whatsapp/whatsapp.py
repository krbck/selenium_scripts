from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def search_and_click(contact_name,message):
    search_box = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[role='textbox'][contenteditable='true']"))
    )
    
    search_box.click()
    search_box.clear() 
    search_box.send_keys(Keys.CONTROL + "a")
    search_box.send_keys(Keys.DELETE)
    search_box.send_keys(contact_name) 
    time.sleep(1) 


    results = wait.until( EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[role='listitem']"))
    )
    print(f"Found {len(results)} results")
    
    for r in results:
        try:
            name_span = r.find_element(By.CSS_SELECTOR, "span[title]")
            name = name_span.get_attribute('title')
            print(name)
            if name == "Furkan":
                 r.click()
                 print(f"Clicked on contact: {name}")
                 
                 message_box = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div[contenteditable='true'][data-tab='10']"))
                )
                 message_box.send_keys(message + Keys.ENTER)
                 print(f"Sent message: {message}")

                 time.sleep(100)
                 break
        except:
                continue

# Start WebDriver
driver = webdriver.Chrome() 
driver.get("https://web.whatsapp.com")

# Wait for QR code login
print("Scan the QR code with your phone...")
# Wait up to 20 seconds for the search box to be present and visible

wait = WebDriverWait(driver, 20)
        
contact_name = input("Enter the contact name: ")
message = input("Enter the message to send: ")

search_and_click(contact_name, message)        