from typing import List, Literal
from pyspedfiscal.campos import CampoDecimal, CampoInteiro, CampoAlphanumerico
from pydantic import Field
from pyspedfiscal._registro import Registro

from pyspedfiscal.bloco_c.registro_c195 import RegistroC195
from pyspedfiscal.bloco_c.registro_c197 import RegistroC197


class RegistroC190(Registro):
    """ Registro Analítico do Documento (código 01, 1B, 04, 55 e 65)  """
    reg: Literal['C190']
    cst_icms: CampoInteiro
    cfop: CampoInteiro
    aliq_icms: CampoDecimal
    vl_opr: CampoDecimal
    vl_bc_icms: CampoDecimal
    vl_icms: CampoDecimal
    vl_bc_icms_st: CampoDecimal
    vl_icms_st: CampoDecimal
    vl_red_bc: CampoDecimal
    vl_ipi: CampoDecimal
    cod_obs: CampoAlphanumerico

    registros_c195: List[RegistroC195] = Field(default_factory=list)
    registros_c197: List[RegistroC197] = Field(default_factory=list)
