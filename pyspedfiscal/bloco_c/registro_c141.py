from pyspedfiscal.campos import CampoDecimal, CampoInteiro
from typing import Literal
from pyspedfiscal.models import Registro


class RegistroC141(Registro):
    """ VENCIMENTO DA FATURA (CÓDIGO 01) """
    reg: Literal['C141']
    num_parc: CampoInteiro
    dt_vcto: CampoInteiro
    vl_parc: CampoDecimal
