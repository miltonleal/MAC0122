import unittest, operator
from fração import Fração

class TestFracao(unittest.TestCase):
    """
        Classe que faz os testes principais do módulo fração.
        O módulo unittest é usado para teste unitários.
        O módulo operator é usado para chamar alguns operadores padrões do Python, como: +, -, pow(), etc...
            Isso porque na sintaxe do unittest precisamos passar essas operações como funções.
    """
    global numerador
    numerador = "num" # Defina aqui qual o nome do atributo da classe Fração que armazena os numeradores.
    global denominador
    denominador = "den" # Defina aqui qual o nome do atributo da classe Fração que armazena os denominadores.
    def test_init(self):
        f = Fração(1, 2)
        self.assertEqual(vars(f), {numerador: 1, denominador: 2}, "Deveria ser 1/2")
        f = Fração(-3, 2)
        self.assertEqual(vars(f), {numerador:-3, denominador:2}, "Deveria ser -3/2")
        f = Fração(1, -2)
        self.assertEqual(vars(f), {numerador:-1, denominador:2}, "Deveria ser -1/2")
        self.assertRaises(ZeroDivisionError, Fração, 1, 0)
        self.assertRaises(TypeError, Fração, 'a', 1)
        self.assertRaises(TypeError, Fração, 1, '1')

    def test_add(self):
        f1 = Fração(1, 2)
        f2 = Fração(3, 2)
        f = f1 + f2
        self.assertEqual(vars(f), {numerador:2, denominador:1}, "Deveria ser 2/1")
        self.assertRaises(TypeError, operator.add, f1, 1)
        self.assertRaises(TypeError, operator.add, f1, 'a')

    def test_sub(self):
        f1 = Fração(1, 2)
        f2 = Fração(3, 2)
        f = f1 - f2
        self.assertEqual(vars(f), {numerador:-1, denominador:1}, "Deveria ser -1/1")
        self.assertRaises(TypeError, operator.sub, f1, 1)

    def test_mul(self):
        f1 = Fração(1, 2)
        f2 = Fração(3, 2)
        f = f1 * f2
        self.assertEqual(vars(f), {numerador:3, denominador:4}, "Deveria ser 3/4")
        self.assertRaises(TypeError, operator.mul, f1, 1)

    def test_truediv(self):
        f1 = Fração(1, 2)
        f2 = Fração(3, 2)
        f = f1 / f2
        self.assertEqual(vars(f), {numerador:1, denominador:3}, "Deveria ser 1/3")
        self.assertRaises(TypeError, operator.truediv, f1, 1)

    def test_pow(self):
        f = Fração(1, 2)
        f_zero = f ** 0
        self.assertEqual(vars(f_zero), {numerador:1, denominador:1}, "Deveria ser 1/1")
        f = Fração(1, 2)
        f_pos = f ** 4
        self.assertEqual(vars(f_pos), {numerador:1, denominador:16}, "Deveria ser 1/16")
        f = Fração(1, 2)
        f_neg = f ** -4
        self.assertEqual(vars(f_neg), {numerador:16, denominador:1}, "Deveria ser 16/1")
        f = Fração(0, 1)
        self.assertRaises(ZeroDivisionError, operator.pow, f, -4)

    def test_eq(self):
        f1 = Fração(1, 2)
        f2 = Fração(1, 2)
        self.assertTrue(f1 == f2, "Deveria ser True")
        self.assertRaises(TypeError, operator.eq, f1, 2)
        self.assertRaises(TypeError, operator.eq, f1, 'a')

    def test_lt(self):
        f1 = Fração(1, 2)
        f2 = Fração(3, 2)
        self.assertTrue(f1 < f2, "Deveria ser True")
        self.assertRaises(TypeError, operator.lt, f1, 2)
        self.assertRaises(TypeError, operator.lt, f1, 'a')

    def test_le(self):
        f1 = Fração(3, 2)
        f2 = Fração(3, 2)
        self.assertTrue(f1 <= f2, "Deveria ser True")
        self.assertRaises(TypeError, operator.le, f1, 2)
        self.assertRaises(TypeError, operator.le, f1, 'a')

    def test_gt(self):
        f1 = Fração(5, 2)
        f2 = Fração(3, 2)
        self.assertTrue(f1 > f2, "Deveria ser True")
        self.assertRaises(TypeError, operator.gt, f1, 2)
        self.assertRaises(TypeError, operator.gt, f1, 'a')

    def test_ge(self):
        f1 = Fração(5, 2)
        f2 = Fração(3, 2)
        self.assertTrue(f1 >= f2, "Deveria ser True")
        self.assertRaises(TypeError, operator.ge, f1, 2)
        self.assertRaises(TypeError, operator.ge, f1, 'a')

    def test_ne(self):
        f1 = Fração(5, 2)
        f2 = Fração(1, 2)
        self.assertTrue(f1 != f2, "Deveria ser True")
        self.assertRaises(TypeError, operator.ne, f1, 2)
        self.assertRaises(TypeError, operator.ne, f1, 'a')

if __name__ == '__main__':
    unittest.main()