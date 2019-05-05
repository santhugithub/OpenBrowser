from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome(executable_path="C:/Users/Satish/PycharmProjects/OpenBrowser/Drivers/chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.implicitly_wait(30)
driver.maximize_window()
date_ele = driver.find_element_by_id("day")
month_ele = driver.find_element_by_id("month")
year = driver.find_element_by_id("year")
select = Select(date_ele)
select.select_by_visible_text("20")
select = Select(month_ele)
select.select_by_visible_text("Jun")
select = Select(year)
select.select_by_visible_text("2000")
