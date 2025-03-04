from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from playsound import playsound

# Asenna ja käynnistä WebDriver automaattisesti
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

URL = "https://app.outlier.ai/en/expert"
ELEMENT_XPATH = "//*[contains(text(), 'Start tasking')]"  # Etsi elementti, jossa on teksti "Start tasking"
REFRESH_INTERVAL = 5*60 # 5 minutes each with 60 seconds

# Attach to the already running Chrome session
options = webdriver.ChromeOptions()
options.debugger_address = "localhost:9222"  # Connect to the opened Chrome

driver = webdriver.Chrome(options=options)  # Use existing Chrome

try:
    driver.get(URL)
    while True:
        try:
            elements = driver.find_elements(By.XPATH, ELEMENT_XPATH)

            if elements:
                print("New task found")
                playsound("output.mp3")
                break
            else:
                print("New task not found, checking again...")
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(REFRESH_INTERVAL)
        driver.refresh()
finally:
    driver.quit()
