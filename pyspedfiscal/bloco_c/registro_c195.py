from typing import Literal
from pyspedfiscal.campos import CampoAlphanumerico
from pyspedfiscal._registro import Registro


class RegistroC195(Registro):
    """ 
    Complemento do Registro Analítico - Observações do Lançamento Fiscal
    (código 01, 1B, 04 e 55) 
    """
    reg: Literal['C195']
    cod_obs: CampoAlphanumerico
    txt_compl: CampoAlphanumerico
