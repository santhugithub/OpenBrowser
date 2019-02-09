from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="F:/Selenium/chromedriver.exe")
driver.get ("F:\Selenium/excersise1.html")
driver.find_element_by_class_name("first").send_keys("santhu.ns.in@gmail.com")
time.sleep(2)
driver.find_element_by_class_name("second").send_keys("thelionking")
time.sleep(3)
driver.find_element_by_class_name("third").click()