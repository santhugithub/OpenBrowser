from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="F:/Selenium/chromedriver.exe")
driver.get("https://in.linkedin.com/")
driver.find_element_by_id("reg-firstname").send_keys("santhu")
time.sleep(2)
driver.find_element_by_id("reg-lastname").send_keys("NS")
time.sleep(2)
driver.find_element_by_id("reg-email").send_keys("santhu.ns.in@gmal.com")
driver.find_element_by_id("reg-password").send_keys("santhu.ns.in@gmal.com")
driver.find_element_by_id("registration-submit").click()
