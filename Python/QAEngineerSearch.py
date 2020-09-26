# Python Selenium work
# 20200722 - For a fake jobsite, searches for 'QA Engineer', prints results.

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "F:\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("thisisafakejobwebsite.tech") # Dummy site
print(driver.title)

search = driver.find_element_by_class("searchfield")
search.send_keys("QA Engineer")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, "main"))
	)

articles = main.find_elements_by_tag_name("article")
for article in articles:
	header = article.find_elements_by_class_name("entry-title")
	print(header.text)

driver.quit()
