import unittest

class TesteExemplo1(unittest.TestCase):
    def teste_adicao(self):
        print("Executando Teste: teste_adicao")
        self.assertEqual(1 + 1, 2)
        print("teste_adicao passou")

    def teste_subtracao(self):
        print("Executando Teste: teste_subtracao")
        self.assertEqual(2 - 1, 1)
        print("teste_subtracao passou")

    def teste_falha_adicao(self):
        print("Executando Teste: teste_falha_adicao")
        self.assertEqual(1 + 1, 3)  # Este teste irá falhar
        print("teste_falha_adicao passou")

if __name__ == "__main__":
    unittest.main()
