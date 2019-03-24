from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.implicitly_wait(10)
driver.maximize_window()
link=driver.find_elements_by_tag_name('a')
print(len(link))
'''
for count in link:
    count'''