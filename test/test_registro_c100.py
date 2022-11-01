from pyspedfiscal.bloco_c.registro_c100 import RegistroC100
import unittest
from pathlib import Path


arquivo_teste = Path(__file__).parent / 'arquivos' / 'arquivo_teste.txt'


class TestSpedFiscal(unittest.TestCase):

    def setUp(self) -> None:
        self.registro_c100_teste_1 = '|C100|1|0|88229|55|00|1|14771|33220707978911000530110010000211711000147722|27072022|27072022|41961,29|2|0|0|41961,29|0|0|0|0|41961,29|2937,29|0|0|0|0|0|0|0|'

    def test_deve_ler_um_registro_c100(self):

        registro_c100 = RegistroC100.ler_registro(self.registro_c100_teste_1)
        self.assertEqual(registro_c100.reg, 'C100')


if __name__ == '__main__':
    unittest.main()
