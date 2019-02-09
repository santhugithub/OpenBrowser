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

driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element_by_id("email").send_keys("santhu.ns.in@gmai.com")
driver.find_element_by_id("pass").send_keys("thelionking")
driver.find_element_by_id("u_0_2").click()