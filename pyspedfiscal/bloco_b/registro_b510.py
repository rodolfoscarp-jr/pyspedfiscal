from ..models import Registro
from typing import Literal
from ..campos import CampoAlphanumerico, CampoEnumerate, CampoCPF


class IndProf(CampoEnumerate):
    habilitado = '0'
    nao_habilitado = '1'


class IndEsc(CampoEnumerate):
    superior = '0'
    medio = '1'


class IndSoc(CampoEnumerate):
    socio = '0'
    nao_socio = '1'


class RegistroB510(Registro):
    reg: Literal['B510']
    ind_prof: IndProf
    ind_esc: IndEsc
    ind_soc: IndSoc
    cpf: CampoCPF
    nome: CampoAlphanumerico
