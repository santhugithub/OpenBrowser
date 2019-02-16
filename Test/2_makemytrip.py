import time

from selenium import webdriver

Browser='Chrome'

if Browser=='Chrome':
    driver=webdriver.Chrome(executable_path="C:/Users/Satish/PycharmProjects/OpenBrowser/Drivers/chromedriver.exe")
elif Browser=='Firefox':
    driver=webdriver.Firefox(executable_path="C:/Users/Satish/PycharmProjects/OpenBrowser/Drivers/geckodriver.exe")
elif Browser=='Ie':
    driver=webdriver.Ie(executable_path="C:/Users/Satish/PycharmProjects/OpenBrowser/Drivers/IEDriverServer.exe")
else:
    print("Provide the appropriate browser name")
driver.get("https://makemytrip.com/")
driver.maximize_window()
driver.implicitly_wait(5) #implicit wait is applied on the driver
driver.find_element_by_id("header_tab_hotels").click()
time.sleep(5)
driver.find_element_by_id("header_tab_holidays").click()
driver.back()
driver.find_element_by_id("header_tab_cabs").click()
time.sleep(5)
driver.forward()
driver.refresh()
