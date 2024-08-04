import unittest

class TestExample2(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(2 * 2, 4)

    def test_division(self):
        self.assertEqual(4 / 2, 2)

if __name__ == "__main__":
    unittest.main()
