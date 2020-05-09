import unittest
import romanos

class RomanNumbertest(unittest.TestCase):

    def test_symbols_romanos(self):
        self.assertEqual(romanos.romano_a_entero('I'), 1)
        self.assertEqual(romanos.romano_a_entero('V'), 5)
        self.assertEqual(romanos.romano_a_entero('X'), 10)
        self.assertEqual(romanos.romano_a_entero('L'), 50)
        self.assertEqual(romanos.romano_a_entero('C'), 100)
        self.assertEqual(romanos.romano_a_entero('D'), 500)
        self.assertEqual(romanos.romano_a_entero('M'), 1000)
        self.assertEqual(romanos.romano_a_entero('K'), 'no existe ese numero romano')
        self.assertEqual(romanos.romano_a_entero(''), 0)
        self.assertEqual(romanos.romano_a_entero('MMMM'), "no cumple regla 3 repeticiones")
        self.assertEqual(romanos.romano_a_entero('MLIV'), "no cumple orden")

if __name__=='__main__':
    unittest.main ()       