import unittest

class TestExample1(unittest.TestCase):
    def test_addition(self):
        print("Running Test: test_addition")
        self.assertEqual(1 + 1, 2)
        print("test_addition passed")

    def test_subtraction(self):
        print("Running Test: test_subtraction")
        self.assertEqual(2 - 1, 1)
        print("test_subtraction passed")

    def test_addition_failure(self):
        print("Running Test: test_addition_failure")
        self.assertEqual(1 + 1, 3)  # Este teste irá falhar
        print("test_addition_failure passed")

if __name__ == "__main__":
    unittest.main()
