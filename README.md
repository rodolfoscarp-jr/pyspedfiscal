# PySpedFiscal

Lê e serializa um arquivo do tipo Sped Fiscal

### Exemplo

Utilize o metodo da classe `importar` para carregar um arquivo seped.

```python
from pyspedfiscal import SpedFiscal

sped_fiscal = SpedFiscal.importar('caminho_arquivo')
```

### Registros Implementados

- [ ] Bloco 0

  - [x] 0000
  - [x] 0001
  - [x] 0200
  - [x] 0460

- [ ] Bloco C

  - [x] C001
  - [x] C100
  - [x] C101
  - [x] C105
  - [x] C110
  - [x] C111
  - [x] C112
  - [x] C113
  - [x] C114
  - [x] C115
  - [x] C116
  - [x] C120
  - [x] C130
  - [x] C140
  - [x] C160
  - [x] C170
  - [x] C180
  - [x] C190
  - [x] C195
  - [x] C197

- [ ] Bloco E

  - [x] E001
  - [x] E100
  - [x] E110
  - [x] E115

- [ ] Bloco 9

  - [x] 9001
  - [x] 9999

### Instalação

- `pip install https://test.pypi.org/simple/pyspedfiscal`

### Dependencias

- Pydantic
