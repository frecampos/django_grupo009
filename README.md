<h1>Casos de Prueba</h1>

NUestro grupo detemino que los casos de prueba que se desar...........................

a) Test de Reg de Clientes

nosotros queneramos las pruebas de eliminacion y agregar en la ........................

Codigo:
class TestCadenas(unittest.TestCase):

    def test_cadenas_iguales(self):
        valor= 9
        self.assertEqual(valor,9)
    
    def test_cadenas_distintas(self):
        self.assertFalse('hola' in 'es un mundo')

b) Test de Insumos
