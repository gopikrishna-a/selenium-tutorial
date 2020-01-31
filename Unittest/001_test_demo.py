import unittest


class TestCaseDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('SetUP Class')

    @classmethod
    def tearDownClass(cls):
        print('tearDown Class')

    def setUp(self):
        print('setup method')

    def tearDown(self):
        print('teardown')

    def test_one(self):
        print('test one')

    def test_two(self):
        print('test two')


unittest.main()


import unittest

from test_cases_one import *
from test_cases_two import *


tc1 = unittest.TestLoader().loadTestsFromTestCase(test_cases_one)
tc2 = unittest.TestLoader().loadTestsFromTestCase(test_cases_two)

ts = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner().run(ts)
