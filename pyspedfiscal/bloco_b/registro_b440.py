from ..models import Registro
from typing import Literal
from ..campos import CampoAlphanumerico, CampoEnumerate, CampoDecimal


class IndOper(CampoEnumerate):
    aquisicao = '0'
    prestacao = '1'


class RegistroB440(Registro):
    reg: Literal['B440']
    ind_oper: IndOper
    cod_part: CampoAlphanumerico
    vl_cont_rt: CampoDecimal
    vl_bc_iss_rt: CampoDecimal
    vl_iss_rt: CampoDecimal
