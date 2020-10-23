from django.test import TestCase
import unittest
from .models import Insumos

# Create your tests here.
class TestCadenas(unittest.TestCase):

    def test_cadenas_iguales(self):
        valor= 9
        self.assertEqual(valor,9)
    
    def test_cadenas_distintas(self):
        self.assertFalse('hola' in 'es un mundo')

class TestInsumos(unittest.TestCase):

    def test_grabar_insumo(self):
        valor = 0
        try:
            insumo = Insumos(
                nombre="xxxx",
                descripcion="limpiador",
                precio=5000,
                stock=1
            )
            insumo.save()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)
    
if __name__ == "__main__":
    unittest.main()