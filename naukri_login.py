from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="F:/Selenium/chromedriver.exe")
driver.get("https://www.naukri.com")
driver.find_elements_by_class_name("registSec").click()
time.sleep(2)
'''driver.find_element_by_id("reg-lastname").send_keys("NS")
time.sleep(2)
driver.find_element_by_id("reg-email").send_keys("santhu.ns.in@gmal.com")
driver.find_element_by_id("reg-password").send_keys("santhu.ns.in@gmal.com")
driver.find_element_by_id("registration-submit").click()'''
