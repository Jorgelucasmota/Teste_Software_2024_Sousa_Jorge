import unittest

class TestExample2(unittest.TestCase):
    def test_multiplication(self):
        print("Running Test: test_multiplication")
        self.assertEqual(2 * 2, 4)
        print("test_multiplication passed")

    def test_division(self):
        print("Running Test: test_division")
        self.assertEqual(4 / 2, 2)
        print("test_division passed")

    def test_division_error(self):
        print("Running Test: test_division_error")
        with self.assertRaises(ZeroDivisionError):
            _ = 1 / 0  # Este teste irá passar, pois espera um erro de divisão por zero
        print("test_division_error passed")

if __name__ == "__main__":
    unittest.main()
