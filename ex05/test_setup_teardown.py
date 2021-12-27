import unittest


def setUpModule():
    print("-> setUpModule called once/module")


def tearDownModule():
    print("-> tearDownModule")


class SetupTeardownDemo(unittest.TestCase):
    customer_id = 56

    @classmethod
    def setUpClass(cls):
        print("---> setUpClass executes only once. CREATE DATABASE;")
        cls.database = "postgres://"

    def setUp(self):
        print()
        print("------->    setUp executes before every test method!")
        self.account_id = 34

    def tearDown(self):
        print("------->    tearDown executes after every test method!")

    @classmethod
    def tearDownClass(cls):
        print("---> tearDownClass executes only once. DROP DATABASE;")

    def test_first_method(self):
        print("        This is the first test. It will PASS")
        self.assertEqual(self.database, "postgres://")
        self.assertTrue(self.account_id == 34)
        assert self.customer_id == 56

    def test_second_method(self):
        print("        This is the second test. It will FAIL")
        assert False

    def test_zzzzz(self):
        print("        This is the last test. It will PASS")
        assert True

    @unittest.skip("setUp/tearDown not executed !!!!")
    def test_skip_me(self):
        pass


class TestFileDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("---> TestFileDemo.setUpClass -> CREATE FILE;")

    @classmethod
    def tearDownClass(cls):
        print("---> TestFileDemo.tearDownClass -> REMOVE FILE;")

    def test_pretend_were_testing_files_on_disk(self):
        pass


if __name__ == "__main__":
    unittest.main()
