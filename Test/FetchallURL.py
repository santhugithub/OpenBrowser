from selenium import webdriver
import requests

driver=webdriver.Chrome()
driver.get("http://google.com")
element=driver.find_elements_by_tag_name("a")
print(type(element))
print(len(element))

broken_link=[]
correct_link=[]

for i in element:
    if (requests.head(i.get_attribute("href")).status_code !=200):
        broken_link.append(i.get_attribute("href"))
    else:
        correct_link.append(i.get_attribute("href"))
print("broken_link",broken_link)
print("correct_link",correct_link)

# for i in element:
# r=requests.head(i.get_attribute("href"))
# if r.status_code !=200
#     print(i) #all the web element is priented
#     print(i.get_attribute("href")) #this get all attribute having href or URL
#     print(requests.head(i.get_attribute("href"))) #gives you the request code 404 like 2xx 3xx
#

