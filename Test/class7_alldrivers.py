from selenium import webdriver

#no need to give the execuitable path coz we have given the path in env variable path
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")


#for firefox
driver=webdriver.Firefox()
driver.get("https://www.facebook.com/")
