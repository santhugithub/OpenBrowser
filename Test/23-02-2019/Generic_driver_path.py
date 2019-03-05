import os
from selenium import webdriver
project_path=os.getcwd() #get the current path of the file
#we are replacing the backword slash coz it wont work in selenium
#in python single backword slash\ is a escape char so we write double\\
driver_path=project_path.replace("\\","/")+"/Drivers" #"Drivers folder path"
print(driver_path)
driver=webdriver.Chrome(executable_path=driver_path+"/chromedriver.exe")
driver.get("http://facebook.com")
