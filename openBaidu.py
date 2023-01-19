from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

#Define the path
driver = webdriver.Edge()
driver.get('https://www.baidu.com')
time.sleep(2)

#Define the elements
searchbox = driver.find_element_by_id('kw')
button = driver.find_element_by_id('su') 
print(searchbox)
print(button)

#Action chain
actions = ActionChains(driver)
actions.move_to_element(searchbox)
actions.click(searchbox)
str = 'opgg'
actions.send_keys_to_element(searchbox,str)
time.sleep(1)

actions.move_to_element(button)
actions.click(button)
time.sleep(1)

#Perform
actions.perform()
time.sleep(1)




