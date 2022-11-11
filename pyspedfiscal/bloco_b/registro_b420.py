from ..models import Registro
from typing import Literal
from ..campos import CampoAlphanumerico, CampoDecimal


class RegistroB420(Registro):
    reg: Literal['B420']
    vl_cont: CampoDecimal
    vl_bc_iss: CampoDecimal
    aliq_iss: CampoDecimal
    vl_isnt_iss: CampoDecimal
    vl_iss: CampoDecimal
    cod_serv: CampoAlphanumerico
