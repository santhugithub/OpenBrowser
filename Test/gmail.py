from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="F:/Selenium/chromedriver.exe")
driver.get("https://www.gmail.com/")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//*[@autocomplete='username' and @class='whsOnd zHQkBf']").send_keys("santoshn.shankar@gmail.com")
driver.find_element_by_xpath("//*[@class='RveJvd snByac']").click()
driver.find_element_by_xpath("//*[@jsname='YPqjbf' and @name='password']").send_keys("appaammasati")
driver.find_element_by_xpath("//*[@class='RveJvd snByac']").click()
driver.find_element_by_xpath("//*[@gh='cm' and @style='user-select: none;']").click()
driver.maximize_window()
handles = driver.window_handles
size=len(handles)
print(size)
print(type(handles)) #The type will be of LIST
parent_handle = driver.current_window_handle # current_window_handle gives you the ID of the current window
print(parent_handle)
for x in range(size):
    if handles[x] != parent_handle:
        driver.switch_to.window(handles[x])
        print(driver.title)
        driver.find_element_by_xpath("//*[@class='Am Al editable LW-avf' and @hidefocus='true']").send_keys("Test")
        time.sleep(5)
        driver.close()
        break




