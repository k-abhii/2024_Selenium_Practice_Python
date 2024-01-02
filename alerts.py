import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
print(driver.title)
print(driver.current_url)
driver.find_element(By.CSS_SELECTOR,"button[onclick='jsPrompt()']").click()
time.sleep(5)
alertwindow = driver.switch_to.alert
print(alertwindow.text)
alertwindow.send_keys("Abhimanyu Kumar")
alertwindow.accept()
# alertwindow.dismiss()
