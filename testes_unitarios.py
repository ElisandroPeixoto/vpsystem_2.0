import unittest
from funcoes import neutro
from classes import Disjuntor


class TestesFuncoes(unittest.TestCase):

    def test_neutro_zero(self):
        self.assertEqual(neutro([120, 0], [120, -120], [120, 120]), (0, 0))

    def test_disjuntor_fechar(self):
        dj = Disjuntor([0, 0], [0, 0], [0, 0])
        self.assertTrue(dj.fechar())

    def test_disjuntor_abrir(self):
        dj = Disjuntor([0, 0], [0, 0], [0, 0], True)
        self.assertFalse(dj.abrir())


if __name__ == "__main__":
    unittest.main()
