from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="F:/Selenium/chromedriver.exe")
#driver.get("http://www.google.com")
#driver.get("https://github.com/")
#driver.get("https://www.facebook.com/")
#driver.get ("F:\Selenium/login.html")
driver.get ("F:\Selenium/excersise1.html")
driver.find_element_by_id("UID").send_keys("santhu.ns.in@gmail.com")
time.sleep(2)
driver.find_element_by_id("PID").send_keys("thelionking")
time.sleep(5)
driver.find_element_by_id("loginid").click()