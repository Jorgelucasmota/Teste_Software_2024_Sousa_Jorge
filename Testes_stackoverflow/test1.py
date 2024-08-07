import unittest

class TesteExemplo1(unittest.TestCase):
    def teste_adicao(self):
        self.assertEqual(1 + 1, 2)

    def teste_subtracao(self):
        self.assertEqual(2 - 1, 1)

if __name__ == "__main__":
    unittest.main()
