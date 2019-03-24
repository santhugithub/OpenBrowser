from selenium import webdriver

driver=webdriver.Chrome()
driver.get("file:///F:/Selenium/practice/webtable.html")
driver.maximize_window()

ele = driver.find_elements_by_xpath("//*[@id='emptable']/thead/tr/th")
a=len(ele)
print("The length of the header is",a)
row1 = driver.find_elements_by_xpath("//*[@id='emptable']/tbody/tr[1]/td") #gives you column count
b=len(row1)
print("The total count of the column is",b)
col = driver.find_elements_by_xpath("//*[@id='emptable']/tbody/tr") #gives you row count
c=len(col)
print("The total length of the row is",c)
d=driver.find_elements_by_xpath("//table/tbody/tr/td[1]")
e=driver.find_elements_by_xpath("//*[@id='emptable']/tbody/tr[2]/td[1]")

print("----------------------------------------------")
for i in ele:
    data=i
    print("the Header data is",data.text)
print("----------------------------------------------")
for i in row1:
    data=i
    print("The value if the row1 is",data.text)
print("----------------------------------------------")
for i in col:
    data=i
    print("The value of the all rows is",data.text)
print("----------------------------------------------")
for i in d:
    print("The 1st column value",i.text)
print("----------------------------------------------")
for i in e:
    print("The empid of satish is ",i.text)
print("----------------------------------------------")



first_part="//*[@id='emptable']/thead/tr/th["
second_part="]"