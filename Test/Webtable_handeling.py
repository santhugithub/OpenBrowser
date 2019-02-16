from selenium import webdriver

driver=webdriver.Chrome()
driver.get("file:///F:/Selenium/practice/webtable.html")
driver.maximize_window()
ele = driver.find_elements_by_xpath("//*[@id='emptable']/thead/tr/th")
print(len(ele))
row1 = driver.find_elements_by_xpath("//*[@id='emptable']/tbody/tr[1]/td") #gives you column count
print(len(row1))
col = driver.find_elements_by_xpath("//*[@id='emptable']/tbody/tr") #gives you row count
print(len(col))
first_part="//*[@id='emptable']/thead/tr/th["
second_part="]"

