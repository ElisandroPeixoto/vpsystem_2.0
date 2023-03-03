import unittest
from funcoes_protecao import neutro
from classes import Disjuntor


class TestesFuncoes(unittest.TestCase):

    # ***** Funcao Calculo do Neutro *****
    def test_neutro_zero(self):
        "Retorna valor de neutro igual a zero"
        self.assertEqual(neutro([120, 0], [120, -120], [120, 120]), (0, 0))

    # ***************************************

    # ***** Abertura e Fechamento do Disjuntor *****
    def test_disjuntor_fechar(self):
        "Fechamento do disjuntor"
        dj = Disjuntor([0, 0], [0, 0], [0, 0])
        self.assertTrue(dj.fechar())

    def test_disjuntor_abrir(self):
        "Abertura do Disjuntor"
        dj = Disjuntor([0, 0], [0, 0], [0, 0], True)
        self.assertFalse(dj.abrir())

    # ***************************************

    # Rele 50 Fase
    def test_funcao_50(self):
        "Atuacao funcao 50"
        dj = Disjuntor([100, 0], [50, -120], [50, 120])
        self.assertTrue(dj.rele50(70))

    def test_funcao_50_2(self):
        "Nao atuacao da funcao 50"
        dj = Disjuntor([20, 0], [30, 0], [20, 0])
        self.assertFalse(dj.rele50(100))

    # ***************************************

    # Rele 50 Neutro
    def test_funcao_50N(self):
        "Atuacao do 50 de Neutro"
        dj = Disjuntor([100, 0], [0, 0], [0, 0])
        self.assertTrue(dj.rele50N(90))

    def test_funcao_50N_2(self):
        "Nao atuacao da funcao 50"
        dj = Disjuntor([0, 0], [0, 0], [1200, 0])
        self.assertFalse(dj.rele50N(1500))

    # ***************************************

    # Rele 51 Fase
    def test_funcao_51(self):
        "Tempo de atuacao correto"
        dj = Disjuntor([1000, 0], [300, -120], [2, 140])
        tempo = dj.rele51(100, 'SI', 0.05)
        if tempo is not None:
            self.assertAlmostEqual(float(tempo), 0.1485, delta=0.9)

    def test_funcao_51n(self):
        "Tempo de atuacao correto de Neutro"
        dj = Disjuntor([1000, 0], [0, 0], [0, 0])
        tempo = dj.rele51N(100, 'SI', 0.05)
        if tempo is not None:
            self.assertAlmostEqual(float(tempo), 0.1485, delta=0.9)
        else:
            self.fail()


if __name__ == "__main__":
    unittest.main()
