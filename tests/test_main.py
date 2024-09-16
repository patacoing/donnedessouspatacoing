import unittest
from donnedessouspatacoing.main import donne_des_sous, compte_en_banque


class MyTestCase(unittest.TestCase):
    def test_something(self):
        compte_en_banque = donne_des_sous(8, 10)
        self.assertEqual(18, compte_en_banque)


    def test_somethin1(self):
        compte_en_banque = donne_des_sous(12, 10)
        self.assertEqual(24, compte_en_banque)


if __name__ == '__main__':
    unittest.main()
