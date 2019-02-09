from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="F:/Selenium/chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.find_element_by_id("u_0_j").send_keys("santhu")
time.sleep(2)
driver.find_element_by_id("u_0_l").send_keys("NS")
time.sleep(2)
driver.find_element_by_id("u_0_o").send_keys("santhu.ns.in@gmal.com")
driver.find_element_by_id("u_0_r").send_keys("santhu.ns.in@gmal.com")
driver.find_element_by_id("u_0_v").send_keys("Kingisalwaysking")
