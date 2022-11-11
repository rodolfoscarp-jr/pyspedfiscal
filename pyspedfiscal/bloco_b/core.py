from typing import List
from ..models import Bloco
from .registro_b001 import RegistroB001
from .registro_b020 import RegistroB020
from .registro_b025 import RegistroB025
from .registro_b030 import RegistroB030
from .registro_b035 import RegistroB035
from .registro_b350 import RegistroB350
from .registro_b420 import RegistroB420
from .registro_b440 import RegistroB440
from .registro_b460 import RegistroB460
from .registro_b470 import RegistroB470
from .registro_b500 import RegistroB500
from .registro_b510 import RegistroB510
from .registro_b990 import RegistroB990


class BlocoB(Bloco):
    def __init__(self):
        self.registro_b001: RegistroB001 = None
        self.registro_b990: RegistroB990 = None

    @classmethod
    def ler_registros(cls, registros: List[str]) -> 'BlocoB':
        bloco = cls()

        for registro in registros:
            tipo_registro = registro[1:5].upper()

        return bloco
