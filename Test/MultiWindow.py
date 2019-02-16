from selenium import  webdriver
import time

Brower=webdriver.Chrome()
Brower.get("https://phptravels.com/")
Brower.maximize_window()
Brower.implicitly_wait(30)
Brower.delete_all_cookies() #delete all the cookies
Current_window_id=Brower.current_window_handle
print(Current_window_id)
time.sleep(10)
Brower.find_element_by_xpath("//span[text()='Login']").click()
Window_ids=Brower.window_handles
print(Window_ids)
print(type(Window_ids))

for handle in Window_ids:
    print(handle)
    if handle != Current_window_id:
        Brower.switch_to.window(handle)
        Brower.find_element_by_name("username").send_keys("TEST")
Brower.close() # close the current tab
Brower.quit()  # close the entire brower opened by the session