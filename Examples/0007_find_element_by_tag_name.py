from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
driver.get('https://facebook.com')
print(driver.find_element_by_tag_name('span').text)
time.sleep(10) # Sleep time to observe
driver.quit()