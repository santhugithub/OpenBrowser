from selenium import webdriver
driver=webdriver.Chrome()
#driver.get("https://www.facebook.com/")
#driver.get("https://in.linkedin.com/")
driver.get("https://www.gmail.com/")
driver.find_element_by_xpath("//span[contains(text(),'Create account')]").click()
driver.implicitly_wait(10)
driver.maximize_window()
# a is for fb page and b is for linkedin page
#a = driver.find_elements_by_xpath("//input[@class='inputtext' or @type='text']")
#b= driver.find_elements_by_xpath("//input[@type='text' or @type='password']")
c= driver.find_elements_by_xpath("//input[@type='text' or @type='password']")
# change the variable value to either a or b in for loop and execute the code
for i in c:
    i.send_keys("Qspiders@gmail.com")



