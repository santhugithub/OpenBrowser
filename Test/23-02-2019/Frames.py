from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.implicitly_wait(10)
frame=driver.find_element_by_tag_name("iframe")
#switching the frames
driver.switch_to.frame(frame)
driver.find_element_by_id("datepicker").click()
#or we can write liike this
#driver.find_element_by_xpath("//input[@id='datepicker']").click()
#switching to the parent frames
driver.switch_to.parent_frame()
#driver.switch_to.default_content()
driver.find_element_by_xpath("//a[text()='Draggable']").click()
# driver.find_element_by_xpath("//a[text()='Accordion']").click()
# driver.switch_to.default_content()
# driver.find_element_by_xpath("//h3[@id='ui-id-3']").click()


