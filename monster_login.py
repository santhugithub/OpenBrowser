from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="F:/Selenium/chromedriver.exe")
driver.get("https://www.monsterindia.com/")
time.sleep(2)
driver.find_element_by_class_name("signinModal").click()
time.sleep(2)
driver.find_element_by_id("firstName_id").send_keys("Santhosh")
driver.find_element_by_id("lastName_id").send_keys("kumar")
time.sleep(2)
driver.find_element_by_id("email").send_keys("santhu.ns.in@gmal.com")
driver.find_element_by_id("passwd_id").send_keys("ineedjob")
driver.find_element_by_id("mobile2").send_keys("6545435461")
driver.find_element_by_id("skills").send_keys("python half knowledge")
driver.find_element_by_id("wordresume").click()




