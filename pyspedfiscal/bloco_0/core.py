from typing import List
from ..models import Bloco
from .registro_0000 import Registro0000


class Bloco0(Bloco):
    def __init__(self):
        self.registro_0000: Registro0000 = None

    @classmethod
    def ler_registros(cls, registros: List[str]) -> 'Bloco0':
        bloco = cls()

        for registro in registros:
            tipo_registro = registro[1:5].upper()

            # Nivel 1 - Registro Pai
            if tipo_registro == '0000':
                bloco.registro_0000 = Registro0000.ler_registro(registro)

        return bloco
