from selenium import webdriver
import time
driver=webdriver.Ie(executable_path="F:/Selenium/IE_browser/IEDriverServer.exe")
driver.get("https://www.facebook.com/")
time.sleep(5)
driver.find_element_by_id("email").send_keys("santhu.ns.in@gmail.com")
time.sleep(2)
driver.find_element_by_id("pass").send_keys("thelionking")
time.sleep(2)
driver.find_element_by_id("loginbutton").click()




