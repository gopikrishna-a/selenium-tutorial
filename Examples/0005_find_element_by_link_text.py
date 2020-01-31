from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
driver.get('https://facebook.com')
element = driver.find_element_by_link_text('Forgotten account?')
element.click()
time.sleep(10) # Sleep time to observe
driver.quit()