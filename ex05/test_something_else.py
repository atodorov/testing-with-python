import unittest


class TestCustomerId(unittest.TestCase):
    customer_id = 56

    def test_id(self):
        self.assertEqual(56, self.customer_id)


if __name__ == "__main__":
    unittest.main()
