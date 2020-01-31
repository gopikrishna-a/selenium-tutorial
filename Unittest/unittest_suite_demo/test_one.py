import unittest


class TestOne(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('TestOne setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('TestOne tearDownClass')

    def setUp(self):
        print('TestOne setup')

    def tearDown(self):
        print('TestOne teardown')

    def test_case_one(self):
        print('TestOne: test case one')

    def test_case_two(self):
        print('TestOne test case two')
