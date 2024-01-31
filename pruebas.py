import unittest
import math
from biblioteca import suma, resta, multiplicacion, division, modulo, conjugado, polar, fase

class TestFuncionesComplejas(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma((2, 3), (1, -2)), (3, 1))
        self.assertEqual(suma((0, 0), (4, 5)), (4, 5))

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion((2, 3), (1, -2)), (8, -1))
        self.assertEqual(multiplicacion((0, 0), (4, 5)), (0, 0))

    def test_resta(self):
        self.assertEqual(resta((2, 3), (1, -2)), (1, 5))
        self.assertEqual(resta((0, 0), (4, 5)), (-4, -5))

    def test_division(self):
        self.assertEqual(division((2, 3), (1, -2)), (-0.8, 1.4))
        self.assertEqual(division((4, 5), (0, 1)), (5, -4))

    def test_modulo(self):
        self.assertAlmostEqual(modulo((3, 4)), 5.0, delta=1e-5)  # Ajusta la tolerancia según tus necesidades
        self.assertAlmostEqual(modulo((-2, 0)), 2.0, delta=1e-5)

    def test_conjugado(self):
        self.assertEqual(conjugado((2, 3)), (2, -3))
        self.assertEqual(conjugado((0, 0)), (0, 0))

    def test_polar(self):
        # Ajusta el valor esperado y la tolerancia según tu implementación y necesidades
        self.assertAlmostEqual(polar((3, 4))[0], 3.0, delta=1e-5)
        self.assertAlmostEqual(polar((3, 4))[1], 4, delta=1e-5)

        self.assertAlmostEqual(polar((-1, 0))[0], 1.0, delta=1e-5)
        self.assertAlmostEqual(polar((-1, 0))[1], 0.0, delta=1e-5)

    def test_fase(self):
        self.assertAlmostEqual(fase((1, math.sqrt(3))), math.pi / 3, places=5)
        self.assertAlmostEqual(fase((1, 0)), 0.0, places=5)

if __name__ == '__main__':
    unittest.main()
