from selenium import webdriver
import time
driver=webdriver.Firefox(executable_path="F:/Selenium/firefox webdriver/geckodriver.exe")
driver.get("https://www.facebook.com/")
driver.find_element_by_id("email").send_keys("santhu.ns.in@gmail.com")
time.sleep(2)
driver.find_element_by_id("pass").send_keys("thelionking")
time.sleep(2)
driver.find_element_by_id("loginbutton").click()




