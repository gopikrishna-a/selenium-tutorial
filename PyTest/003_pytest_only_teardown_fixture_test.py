import pytest

# Pytest only teardown fiixture example
class TestFixtureDemo():

    @pytest.yield_fixture()
    def my_teardown(self):
        yield
        print('Teardown fixture activity')

    def test_one(self, my_teardown):
        print('test one')

    def test_two(self, my_teardown):
        print('test two')