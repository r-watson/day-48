from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "https://www.python.org/"
chrome_driver_path = "C:\Programming\Web Driver\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(url)

# get text from element by ID
# price = driver.find_element(By.ID, "priceblock_ourprice")
# print(price.text)

# find_element(By.NAME) is useful for filling out forms as they usually have descriptive names.
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# useful for getting elements that don't have a class name or ID directly.
# e.g. inside the documentation-widget class find an anchor tag. can be any number of levels deeper. don't have to specify the whole path.
# documentation_link =driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# xpath directly to element. copy xpath from chrome dev tool. xpath has double quotes. so use single quotes.
# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# use find_elements to local all of the instances on the current page.

# upcoming_event_dates = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time')
# upcoming_event_names = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')

# print(list(zip(upcoming_event_dates, upcoming_event_names)))
# new_dict = {key: {'time': date, 'name': name} for (key, name) in len(upcoming_event_names)}
# upcoming_event_dates = [dates.text for dates in upcoming_event_dates]
# upcoming_event_names = [names.text for names in upcoming_event_names]
# new_dict = {i: {'time': upcoming_event_dates[i], 'name': upcoming_event_names[i]} for i in range(len(upcoming_event_names))}
# print(new_dict)
#
#
upcoming_event_dates = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
upcoming_event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')

# for n in range(len(upcoming_event_dates)):
#     events[n] = {
#         'time': upcoming_event_dates[n].text,
#         'name': upcoming_event_names[n].text,
#     }
events = {n: {'time': upcoming_event_dates[n].text, 'name': upcoming_event_names[n].text} for n in range(len(upcoming_event_dates))}
print(events)

# closes one tab:
# driver.close()
# quit all tabs in the browser:
driver.quit()
