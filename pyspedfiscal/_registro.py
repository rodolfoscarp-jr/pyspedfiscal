from abc import ABC
from pydantic import BaseModel
from pyspedfiscal.exception import ValorCampoInvalido, LinhaRegistroInvalida, TamanhoRegistroInvalido


class Registro(BaseModel, ABC):
    @classmethod
    def ler_registro(cls, linha: str):
        valores = linha.split("|")[1:-1]

        # Os campos iniciados com registros_ são filhos do registro
        campos = [campo for campo in cls.__fields__.keys(
        ) if not campo.startswith('registros_')]

        # Checa o o tamnho do registro
        if len(campos) != len(valores):
            print(len(campos), len(valores))
            print(campos)
            print(valores)

            raise TamanhoRegistroInvalido(
                f'Registro com tamanho inválido. \n {linha}')

        valores_dict = dict(list(zip(campos, valores)))

        try:
            return cls(**valores_dict)
        except ValorCampoInvalido as e:
            raise LinhaRegistroInvalida(f'Linha invalida.\n{linha}\n{e}')
