from decimal import Decimal
from datetime import date
import unittest
from pyspedfiscal.tabelas import CodMod, CodSit
from pyspedfiscal.bloco_c import BlocoC
from pyspedfiscal.bloco_c.registro_c001 import IndMov
from pyspedfiscal.bloco_c.registro_c100 import IndOper, IndEmit, IndPgto, IndFrt
from pyspedfiscal.bloco_c.registro_c105 import Oper
from pyspedfiscal.bloco_c.registro_c111 import IndProc
from pyspedfiscal.bloco_c.registro_c112 import CodDA
from pyspedfiscal.bloco_c.registro_c113 import IndOper, IndEmit


class TestBlocoC(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:

        bloco = """
|C001|0|
|C100|1|1|1|55|00|1|1|33220714028298000152550010000000011000147724|27072022|27072022|41961,29|2|0|0|41961,29|0|10|20|30|40|50|60|70|80|90|100|110|120|
|C101|100|20|80|
|C105|0|RJ|
|C110|1|Descricao Complementar Teste|
|C111|Processo Teste|0|
|C112|0|RJ|3|1000|100|01072022|31072022|
|C113|0|0|1|01|001||1|01072022||
|C114|02|1|1|1|01072022|
|C116|59|1|33220714028298000152570010000002110001477205|1|01072022|
|C170|2|1||381,563|UN|2896,06|0|0|060|5101|1653002|0|0|0|0|0|0||||0|0|0|49|2896,06|0,35|0|0|10,14|49|2896,06|0,35|0|0|10,14|4212|0|
|C190|060|5101|0|0|0|0|0|0|0|0||
|C195|1|FECP referente ao diferencial de al�quotas|
|C197|SP10090718|FECP referente ao diferencial de al�quotas||3256,23|0|596,98|0|
|C100|1|1|2|55|00|001|2|33220714028298000152550010000000021000147721|27072022|27072022|41961,29|2|0|0|41961,29|0|0|0|0|0|0|0|0|0|0|0|0|0|
|C170|2|2||381,563|KG|2896,06|0|0|060|5102|1653002|0|0|0|0|0|0||||0|0|0|49|2896,06|0,35|0|0|10,14|49|2896,06|0,35|0|0|10,14|4212|0|
|C190|060|5102|0|0|0|0|0|0|0|0||
|C195|1|FECP referente ao diferencial de al�quotas|
|C197|SP10090718|FECP referente ao diferencial de al�quotas||3256,23|0|596,98|0|
|C100|1|1|3|55|00|001|3|33220714028298000152550010000000031000147729|27072022|27072022|41961,29|2|0|0|41961,29|0|0|0|0|0|0|0|0|0|0|0|0|0|
|C170|2|3||381,563|KG|2896,06|0|0|060|5102|1653002|0|0|0|0|0|0||||0|0|0|49|2896,06|0,35|0|0|10,14|49|2896,06|0,35|0|0|10,14|4212|0|
|C190|060|5102|0|0|0|0|0|0|0|0||
|C195|1|FECP referente ao diferencial de al�quotas|
|C197|SP10090723|FECP referente ao diferencial de al�quotas||3256,23|0|596,98|0|
|C100|1|1|4|55|00|001|4|33220714028298000152550010000000041000147726|27072022|27072022|41961,29|2|0|0|41961,29|0|0|0|0|0|0|0|0|0|0|0|0|0|
|C170|2|4||381,563|KG|2896,06|0|0|060|5104|1653002|0|0|0|0|0|0||||0|0|0|49|2896,06|0,35|0|0|10,14|49|2896,06|0,35|0|0|10,14|4212|0|
|C190|060|5104|0|0|0|0|0|0|0|0||
|C195|1|FECP referente ao diferencial de al�quotas|
|C197|SP10090718|FECP referente ao diferencial de al�quotas||3256,23|0|596,98|0|
|C100|1|1|5|55|00|001|5|33220714028298000152550010000000051000147731|27072022|27072022|41961,29|2|0|0|41961,29|0|0|0|0|0|0|0|0|0|0|0|0|0|
|C170|2|5||381,563|UN|2896,06|0|0|060|5101|1653002|0|0|0|0|0|0||||0|0|0|49|2896,06|0,35|0|0|10,14|49|2896,06|0,35|0|0|10,14|4212|0|
|C190|060|5101|0|0|0|0|0|0|0|0||
|C195|1|FECP referente ao diferencial de al�quotas|
|C197|SP10090722|FECP referente ao diferencial de al�quotas||3256,23|0|596,98|0|
|C100|1|0|1|01|00||1||01072022|01072022|110|0|0|||0|0||0|1000||10|||0|0|||
|C110|1||
|C115|0|11111111111111|12313|12345678909|1100031|22222222222222|123||1100031|
|C990|35|""".splitlines()

        cls.bloco_c = BlocoC.ler_registros(bloco)

    def test_deve_ler_um_registro_c001(self):
        registro_c001 = self.bloco_c.registro_c001

        # |C001|0|

        self.assertEqual(registro_c001.reg, 'C001')
        self.assertEqual(registro_c001.ind_mov, IndMov.com_movimento)

    def test_deve_ler_um_registro_c100(self):

        registro_c100 = self.bloco_c.registro_c001.registros_c100[0]

        # |C100|1|1|1|55|00|1|1|33220714028298000152550010000000011000147724|27072022|27072022|41961,29|2|0|0|41961,29|0|10|20|30|40|50|60|70|80|90|100|110|120|

        self.assertEqual(registro_c100.reg, 'C100')
        self.assertEqual(registro_c100.ind_oper, IndOper.saida)
        self.assertEqual(registro_c100.ind_emit, IndEmit.terceiros)
        self.assertEqual(registro_c100.cod_part, '1')
        self.assertEqual(registro_c100.cod_mod, CodMod.nota_fiscal_eletronica)
        self.assertEqual(registro_c100.cod_sit, CodSit.regular)
        self.assertEqual(registro_c100.ser, '001')
        self.assertEqual(registro_c100.num_doc, 1)
        self.assertEqual(registro_c100.chv_nfe, 33220714028298000152550010000000011000147724)
        self.assertEqual(registro_c100.dt_doc, date(2022, 7, 27))
        self.assertEqual(registro_c100.dt_e_s, date(2022, 7, 27))
        self.assertEqual(registro_c100.vl_doc, Decimal('41961.29'))
        self.assertEqual(registro_c100.ind_pgto, IndPgto.outros)
        self.assertEqual(registro_c100.vl_desc, 0)
        self.assertEqual(registro_c100.vl_abat_nt, 0)
        self.assertEqual(registro_c100.vl_merc, Decimal('41961.29'))
        self.assertEqual(registro_c100.ind_frt, IndFrt.por_conta_do_remetente)
        self.assertEqual(registro_c100.vl_frt, Decimal('10.0'))
        self.assertEqual(registro_c100.vl_seg, Decimal('20.0'))
        self.assertEqual(registro_c100.vl_out_da, Decimal('30.0'))
        self.assertEqual(registro_c100.vl_bc_icms, Decimal('40.0'))
        self.assertEqual(registro_c100.vl_icms, Decimal('50.0'))
        self.assertEqual(registro_c100.vl_bc_icms_st, Decimal('60.0'))
        self.assertEqual(registro_c100.vl_icms_st, Decimal('70.0'))
        self.assertEqual(registro_c100.vl_ipi, Decimal('80.0'))
        self.assertEqual(registro_c100.vl_pis, Decimal('90.0'))
        self.assertEqual(registro_c100.vl_cofins, Decimal('100.0'))
        self.assertEqual(registro_c100.vl_pis_st, Decimal('110.0'))
        self.assertEqual(registro_c100.vl_cofins_st, Decimal('120.0'))

    def test_deve_ler_um_registro_c101(self):

        registro_c101 = self.bloco_c.registro_c001.registros_c100[0].registros_c101

        # |C101|100|20|80|

        self.assertEqual(registro_c101.vl_fcp_uf_dest, Decimal('100'))
        self.assertEqual(registro_c101.vl_icms_uf_dest, Decimal('20'))
        self.assertEqual(registro_c101.vl_icms_uf_rem, Decimal('80'))

    def test_deve_ler_um_registro_c105(self):
        registro_c105 = self.bloco_c.registro_c001.registros_c100[0].registros_c105

        # |C105|0|RJ|

        self.assertEqual(registro_c105.reg, 'C105')
        self.assertEqual(registro_c105.oper, Oper.combustiveis_lubrificantes)
        self.assertEqual(registro_c105.uf, 'RJ')

    def test_deve_ler_um_registro_c110(self):
        registro_c110 = self.bloco_c.registro_c001.registros_c100[0].registros_c110[0]

        # |C110|1|Descricao Complementar Teste|

        self.assertEqual(registro_c110.reg, 'C110')
        self.assertEqual(registro_c110.cod_inf, '1')
        self.assertEqual(registro_c110.txt_compl, 'Descricao Complementar Teste')

    def test_deve_ler_um_registro_c111(self):

        registro_c111 = self.bloco_c.registro_c001.registros_c100[0].registros_c110[0].registros_c111[0]

        # |C111|Processo Teste|0|

        self.assertEqual(registro_c111.reg, 'C111')
        self.assertEqual(registro_c111.num_proc, 'Processo Teste')
        self.assertEqual(registro_c111.ind_proc, IndProc.sefaz)

    def test_deve_ler_um_registro_c112(self):
        registro_c112 = self.bloco_c.registro_c001.registros_c100[0].registros_c110[0].registros_c112[0]

        # |C112|0|RJ|3|1000|100|01072022|31072022|

        self.assertEqual(registro_c112.reg, 'C112')
        self.assertEqual(registro_c112.cod_da, CodDA.documento_estadual)
        self.assertEqual(registro_c112.uf, 'RJ')
        self.assertEqual(registro_c112.num_da, '3')
        self.assertEqual(registro_c112.cod_aut, '1000')
        self.assertEqual(registro_c112.vl_da, Decimal('100'))
        self.assertEqual(registro_c112.dt_vcto, date(2022, 7, 1))
        self.assertEqual(registro_c112.dt_pgto, date(2022, 7, 31))

    def test_deve_ler_um_registro_c113(self):
        registro_c113 = self.bloco_c.registro_c001.registros_c100[0].registros_c110[0].registros_c113[0]

        # |C113|0|0|1|01|001||1|01072022||

        self.assertEqual(registro_c113.reg, 'C113')
        self.assertEqual(registro_c113.ind_oper, IndOper.entrada)
        self.assertEqual(registro_c113.ind_emit, IndEmit.emissao_propria)
        self.assertEqual(registro_c113.cod_part, '1')
        self.assertEqual(registro_c113.cod_mod, CodMod.nota_fiscal)
        self.assertEqual(registro_c113.ser, '001')
        self.assertEqual(registro_c113.sub, None)
        self.assertEqual(registro_c113.num_doc, 1)
        self.assertEqual(registro_c113.dt_doc, date(2022, 7, 1))
        self.assertEqual(registro_c113.chv_doce, None)

    def test_deve_ler_um_registro_c114(self):
        registro_c114 = self.bloco_c.registro_c001.registros_c100[0].registros_c110[0].registros_c114[0]

        # |C114|02|1|1|1|01072022|

        self.assertEqual(registro_c114.reg, 'C114')
        self.assertEqual(registro_c114.cod_mod, CodMod.nota_fiscal_de_venda_consumidor)
        self.assertEqual(registro_c114.ecf_fab, '1')
        self.assertEqual(registro_c114.ecf_cx, 1)
        self.assertEqual(registro_c114.num_doc, 1)
        self.assertEqual(registro_c114.dt_doc, date(2022, 7, 1))

    def test_deve_ler_um_registro_c115(self):
        registro_c115 = self.bloco_c.registro_c001.registros_c100[-1].registros_c110[0].registros_c115[0]

        # |C115|0|11111111111111|12313|12345678909|1100031|22222222222222|123||1100031|

        self.assertEqual(registro_c115.reg, 'C115')


if __name__ == '__main__':
    unittest.main()
