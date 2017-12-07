from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
import time

driver = webdriver.Firefox()

driver.get("http://www.baidu.com")

time.sleep(5)

driver.find_element_by_id("kw").send_keys("TestArt zhihuzhuanlan")
time.sleep(3)
driver.find_element_by_id("su").send_keys(Keys.ENTER)
time.sleep(3)

driver.close()
