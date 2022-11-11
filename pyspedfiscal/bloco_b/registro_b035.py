from ..models import Registro
from typing import Literal
from ..campos import CampoAlphanumerico, CampoDecimal


class RegistroB035(Registro):
    reg: Literal['B035']
    vl_cont_p: CampoDecimal
    vl_bc_iss_p: CampoDecimal
    aliq_iss: CampoDecimal
    vl_iss_p: CampoDecimal
    vl_isnt_iss_p: CampoDecimal
    cod_serv: CampoAlphanumerico
