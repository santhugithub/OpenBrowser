import time
from selenium import webdriver

browser = 'chrome'

if browser == 'chrome':
    driver = webdriver.Chrome(executable_path="C:/Users/Satish/PycharmProjects/OpenBrowser/Drivers/chromedriver.exe")
    # driver = webdriver.Chrome()
    # driver.get("https://www.makemytrip.com/")
elif browser == 'firefox':
    driver = webdriver.Firefox(executable_path="C:/Users/Satish/PycharmProjects/OpenBrowser/Drivers/geckodriver.exe")
    # driver = webdriver.Firefox()
    # driver.get("https://www.makemytrip.com/")
elif browser == 'ie':
    driver = webdriver.Ie(executable_path="C:/Users/Satish/PycharmProjects/OpenBrowser/Drivers/IEDriverServer.exe")
    # driver = webdriver.Ie()
else:
    print("Error - Provide appropriate browser name")

driver.get("https://phptravels.com/demo/")
driver.implicitly_wait(30)
driver.maximize_window()
driver.find_element_by_xpath("//*[@class='login']").click()
time.sleep(5)
handles = driver.window_handles; #window_handles gives you the ID of all the window ID
#here we have 2 windows
size = len(handles)
print(type(handles)) #The type will be of LIST
print(size)
parent_handle = driver.current_window_handle # current_window_handle gives you the ID of the current window
print(parent_handle)
for x in range(size):
    if handles[x] != parent_handle:
        driver.switch_to.window(handles[x])
        print(driver.title)
        driver.find_element_by_xpath("//*[@name='username']").send_keys("Test")
        time.sleep(5)
        driver.close()
        break
'''
driver.switch_to.window(parent_handle);
driver.find_element_by_xpath("//*[@class='login']").click()
time.sleep(10)
driver.quit()
'''