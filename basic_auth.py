import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
print(driver.title)
print(driver.current_url)
time.sleep(5)
# INJECTION
driver.maximize_window()
