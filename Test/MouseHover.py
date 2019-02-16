from selenium import webdriver
import time


Brower=webdriver.Chrome()
Brower.get("https://www.flipkart.com/")
Brower.maximize_window()
Brower.implicitly_wait(30)
time.sleep(15)
element=Brower.find_element_by_xpath("//span[text()='Men']")
webdriver.ActionChains(Brower).move_to_element(element).click(element).perform()