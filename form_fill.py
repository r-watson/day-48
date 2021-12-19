from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "http://secure-retreat-92358.herokuapp.com/"
chrome_driver_path = "C:\Programming\Web Driver\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(url)

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Robert")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Watson")
email = driver.find_element(By.NAME, "email")
email.send_keys("rwatson@fake.net")
sign_up = driver.find_element(By.CSS_SELECTOR, ".form-signin .btn")
sign_up.click()