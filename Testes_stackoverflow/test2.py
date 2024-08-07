import unittest

class TesteExemplo2(unittest.TestCase):
    def teste_multiplicacao(self):
        self.assertEqual(2 * 2, 4)

    def teste_divisao(self):
        self.assertEqual(4 / 2, 2)

if __name__ == "__main__":
    unittest.main()
