# Ejercicio práctico - Unidad 10

import unittest
from calculadora import calculadora as c


class test_calculadora(unittest.TestCase):
    
    def test_suma(self):
        suma1 = c.sumar(2, 2)
        self.assertEqual(suma1, 4)

        suma2 = c.sumar(10, 10)
        self.assertEqual(suma2, 20)

        suma3 = c.sumar(1, -1)
        self.assertEqual(suma3, 0)

    
    def test_resta(self):
        resta1 = c.restar(15, 10)
        self.assertEqual(resta1, 5)

        resta2 = c.restar(10, 100)
        self.assertEqual(resta2, -90)

        resta3 = c.restar(-1, -9)
        self.assertEqual(resta3, 8)

        
    def test_multi(self):
        multi1 = c.multiplicar(2, 2)
        self.assertEqual(multi1, 4)

        multi2 = c.multiplicar(4, 10)
        self.assertEqual(multi2, 40)

        multi3 = c.multiplicar(40, 100)
        self.assertEqual(multi3, 4000)

    
    def test_div(self):
        div1 = c.dividir(10, 5)
        self.assertEqual(div1, 2)
        
        div2 = c.dividir(8, 5)
        self.assertEqual(div2, 1.6)
        
        div3 = c.dividir(2, 5)
        self.assertEqual(div3, 0.4)

