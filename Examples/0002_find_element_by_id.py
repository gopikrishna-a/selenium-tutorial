from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
driver.get('https://www.facebook.com/')
element = driver.find_element_by_id('email')
element.send_keys('helloworld')
time.sleep(10)# Sleep time to observe
driver.quit()