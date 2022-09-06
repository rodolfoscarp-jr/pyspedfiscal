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
  - [x] C170
  - [x] C190
  - [x] C195
  - [x] C197

- [ ] Bloco 9

  - [x] 9001
  - [x] 9999

### Instalação

- `pip install pyspedfiscal`

### Dependencias

- Pydantic
