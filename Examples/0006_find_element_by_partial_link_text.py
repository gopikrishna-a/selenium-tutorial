from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
driver.get('https://facebook.com')
element = driver.find_element_by_partial_link_text('Forgot')
element.click()
time.sleep(10) # Sleep time to observe
driver.quit()