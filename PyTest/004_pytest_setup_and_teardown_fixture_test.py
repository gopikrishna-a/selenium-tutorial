import pytest

class TestFixtureDemo():

    @pytest.yield_fixture()
    def setup_tearndown_fixture(self):
        print('setup activity')
        yield
        print('teardown activity')

    def test_one(self, setup_tearndown_fixture):
        print('test one')

    def test_two(self, setup_tearndown_fixture):
        print('test two')