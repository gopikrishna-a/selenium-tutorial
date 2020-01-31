import pytest


class TestFixtureDemo():

    @pytest.yield_fixture(scope='class')
    def setup_and_teardown_class(self):
        print('setup class activity')
        yield
        print('teardown class activity')

    def test_one(self, setup_and_teardown_class):
        print('test one')

    def test_two(self, setup_and_teardown_class):
        print('test two')
