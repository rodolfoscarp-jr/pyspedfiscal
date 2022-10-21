# PySpedFiscal

Lê e serializa um arquivo do tipo Sped Fiscal

### Exemplo

```python
from pyspedfiscal import SpedFiscal

sped_fiscal = SpedFiscal()
sped_fiscal.importar_arquivo('/PATH')
```

### Registros Implementados

- [ ] Bloco 0

  - [x] 0000

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

- [ ] Bloco 9

  - [x] 9001
  - [x] 9999

### Instalação

- `pip install https://test.pypi.org/simple/pyspedfiscal`

### Dependencias

- Pydantic
