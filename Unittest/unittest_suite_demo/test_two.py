import unittest


class TestTwo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('TestTwo setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('TestTwo tearDownClass')

    def setUp(self):
        print('TestTwo setup')

    def tearDown(self):
        print('TestTwo teardown')

    def test_case_one(self):
        print('TestTwo: test case one')

    def test_case_two(self):
        print('TestTwo test case two')

