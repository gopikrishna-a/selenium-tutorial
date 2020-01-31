import unittest
from test_one import *
from test_two import *


# If you want to execute all test cases in different files we can use following test suite approach
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestOne)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestTwo)

ts = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner().run(ts)