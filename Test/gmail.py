from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://www.gmail.com/")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//*[@autocomplete='username' and @class='whsOnd zHQkBf']").send_keys("santoshn.shankar@gmail.com")
driver.find_element_by_xpath("//*[@class='RveJvd snByac']").click()
driver.find_element_by_xpath("//*[@jsname='YPqjbf' and @name='password']").send_keys("appaammasati")
driver.find_element_by_xpath("//*[@class='RveJvd snByac']").click()
driver.find_element_by_xpath("//*[@gh='cm' and @style='user-select: none;']").click()
driver.maximize_window()
driver.find_element_by_xpath("//*[@class='aoD hl' and @tabindex='1']").click()
driver.find_element_by_xpath("//*[@class='vO' and @aria-label='To' and @rows='1' and @autocorrect='off']").send_keys("srishti24sharma1992@gmail.com")
driver.find_element_by_xpath("//*[@name='subjectbox' and @aria-label='Subject']").send_keys("1 4 3")
driver.find_element_by_xpath("//*[@hidefocus='true' and @aria-label='Message Body']").send_keys("As subject says i may 'hate' or 'love' you. What do you think!!?")
driver.find_element_by_xpath("//*[@role='button' and @data-tooltip='Send ‪(Ctrl-Enter)‬']").click()
time.sleep(10)

