from datetime import date
from pyspedfiscal.bloco_b import BlocoB
from pyspedfiscal.bloco_b.registro_b001 import IndDad
import unittest


class TestBlocoB(unittest.TestCase):

    def setUp(self) -> None:

        bloco = """
|B001|0|
|B020|0|1|1|55|00||10|33220714028298000152550010000000011000147724|01072022|1100064|110|11|10|11|11|10|10|20|11|1|
|B025|10|2|10|10|10|0104|
|B030|3A|1|1|10|01072022|1|100|10|10|10|1|
|B035|10|10|10|12|22|3501|
|B350|10|Conta Teste|71707002|10|0102|100|10|10|111|1|
|B420|200|10|10|110|10|2201|
|B440|0|2|100|11|100|
|B440|1|3|1000|20|22|
|B460|2|1525|22|2|Decricao Teste|1|0|
|B470|100|10|10|20|30|22|1|33|20|10|10|10|10|10|
|B500|100|1|100|
|B990|13|
""".splitlines()

        self.bloco_b = BlocoB.ler_registros(bloco)

    def test_deve_ler_um_registro_b001(self):

        pass


if __name__ == '__main__':
    unittest.main()
