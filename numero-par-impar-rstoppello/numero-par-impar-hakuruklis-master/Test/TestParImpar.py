from app.main import ParImpar
import unittest


class TestPar_o_Impar(unittest.TestCase):
    def TestPar_o_Impar(self):
        self.assertEquals(ParImpar(5),False)
        self.assertEquals(ParImpar(6),True)

if __name__ == '__main__':
    unittest.main()