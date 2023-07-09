# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Opening linkedin Website
driver.get("https://www.linkedin.com")
time.sleep(3)

# Giving username and password

search_bar = driver.find_element("xpath", "/html/body/main/section[1]/div/div/form/div[1]/div[1]/div/div/input")
search_bar.send_keys("juliasuzannemathew@gmail.com")
search_bar.send_keys(Keys.RETURN)
time.sleep(3)
search_bar = driver.find_element("xpath", "/html/body/main/section[1]/div/div/form/div[1]/div[2]/div/div/input")
search_bar.send_keys("Julia@97")
search_bar.send_keys(Keys.RETURN)
time.sleep(5)


# Search for Tata Consultancy Services
search_bar = driver.find_element("xpath", "/html/body/div[5]/header/div/div/div/div[1]/input")
search_bar.send_keys("Tata Consultancy Services")
search_bar.send_keys(Keys.RETURN)
time.sleep(5)

# View Page
search_bar = driver.find_element("xpath", "/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/div/ul/li/div/a/div/div[2]/div[2]/a/div/span/span[1]")
search_bar.click()
time.sleep(5)

# Open Page Website
search_bar = driver.find_element("xpath", "/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[2]/div[3]/div[1]/div[1]/a/span")
search_bar.click()
time.sleep(5)

driver.close()