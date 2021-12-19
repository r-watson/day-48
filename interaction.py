from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://en.wikipedia.org/wiki/Main_Page"
chrome_driver_path = "C:\Programming\Web Driver\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(url)

# find the first anchor tag inside the ID articlecount. Print out the text.
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)
# article_count.click()

# click on the link with the text specified
all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# all_portals.click()

# type in specified text and press enter
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.quit()

