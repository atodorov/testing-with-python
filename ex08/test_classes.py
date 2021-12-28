import unittest


class TestMe(unittest.TestCase):
    def test_less_than(self):
        assert True


class TestWhichDoesnNotInheritFromUnittestTestCase:
    """
        This will be executed only when the test-classes plugin
        is enabled (True by default), see:
        https://docs.nose2.io/en/latest/plugins/testclasses.html
    """
    def test_something_else(self):
        assert False
