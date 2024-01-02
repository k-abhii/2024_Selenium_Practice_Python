import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://mypage.rediff.com/login/dologin")
driver.find_element(By.CSS_SELECTOR,"input[value='Login']").click()
time.sleep(2)
alertwindow = driver.switch_to.alert
print(alertwindow.text)
alertwindow.dismiss()