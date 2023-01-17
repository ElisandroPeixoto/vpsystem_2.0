import unittest
from funcoes import neutro
from classes import Disjuntor


class TestesFuncoes(unittest.TestCase):

    def test_neutro_zero(self):
        "Retorna valor de neutro igual a zero"
        self.assertEqual(neutro([120, 0], [120, -120], [120, 120]), (0, 0))

    def test_disjuntor_fechar(self):
        "Fechamento do disjuntor"
        dj = Disjuntor([0, 0], [0, 0], [0, 0])
        self.assertTrue(dj.fechar())

    def test_disjuntor_abrir(self):
        "Abertura do Disjuntor"
        dj = Disjuntor([0, 0], [0, 0], [0, 0], True)
        self.assertFalse(dj.abrir())

    def test_funcao_50(self):
        "Atuacao funcao 50"
        dj = Disjuntor([100, 0], [50, -120], [50, 120])
        self.assertTrue(dj.rele50(70))

    def test_funcao_50_2(self):
        "Nao atuacao da funcao 50"
        dj = Disjuntor([0, 0], [0, 0], [0, 0])
        self.assertFalse(dj.rele50(100))

    def test_funcao_50N(self):
        "Atuacao do 50 de Neutro"
        dj = Disjuntor([100, 0], [0, 0], [0, 0])
        self.assertTrue(dj.rele50N(90))

    def test_funcao_50N_2(self):
        "Nao atuacao da funcao 50"
        dj = Disjuntor([0, 0], [0, 0], [1200, 0])
        self.assertFalse(dj.rele50N(1500))


if __name__ == "__main__":
    unittest.main()
