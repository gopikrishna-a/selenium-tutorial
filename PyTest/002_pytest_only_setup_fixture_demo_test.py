import pytest


# Pytest example with setup fixture

class TestFixtureDemo():

    @pytest.fixture()
    def my_setup(self):
        print('setup fixture activity')

    def test_one(self, my_setup):
        print('test one')

    def test_two(self, my_setup):
        print('test two')