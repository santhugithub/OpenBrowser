from selenium import webdriver
import time

#-----------------------setting for security testing------------
PROXY = "localhost:1231" #IP:PORT or HOST:PORT
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)

driver=webdriver.Chrome(options=chrome_options)
#-----------------------complete of security testing------------

#driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.implicitly_wait(30)
driver.find_element_by_xpath("//*[@class='inputtext']").send_keys("santhu.ns.in@gmal.com")
driver.find_element_by_xpath("//*[@data-testid='royal_pass']").send_keys("theking")
driver.find_element_by_xpath("//*[@value='Log In']").click()
driver.back()
driver.maximize_window()
driver.find_element_by_xpath("//*[@aria-label='First name']").send_keys("kumar")
driver.find_element_by_xpath("//*[@type='text' and @aria-required='true' and @aria-label='Surname']").send_keys("NS")
driver.find_element_by_xpath("//*[@name='reg_email__']").send_keys("abc@abc.com")
driver.find_element_by_xpath("//*[@aria-label='Re-enter email address']").send_keys("abc@abc.com")
driver.find_element_by_xpath("//*[@name='reg_passwd__' and @aria-label='New password']").send_keys("sfg")
driver.find_element_by_xpath("//*[@name='websubmit']").click()
