import unittest
import time
from selenium import webdriver


# class TestCaseDemo(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         global driver
#         driver = webdriver.Firefox(executable_path='geckodriver')
#         driver.get('https://www.facebook.com')
#         driver.maximize_window()
#
#     @classmethod
#     def tearDownClass(cls):
#         print('tearDown Class')
#         driver.quit()
#
#     def setUp(self):
#         print('setup method')
#
#     def tearDown(self):
#         print('teardown')
#
#     def test_one(self):
#         print('test one')
#         driver.find_element_by_css_selector(By.CSS_SELECTOR, 'input[type="email"]').send_keys('xyz@abc.com')
#         driver.find_element_by_css_selector('input[type="password"]').send_keys('mypassword')
#         driver.find_element_by_css_selector('input[type="submit"]').click()
#         time.sleep(10)

import unittest


class TestOrder(unittest.TestCase):

    def test_B(self):
        print('Test B')

    def test_C(self):
        print('Test C')

    def test_A(self):
        print('Test A')

unittest.main()