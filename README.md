# PySpedFiscal

Lê e serializa um arquivo do tipo Sped Fiscal

### Exemplo

```python
from pyspedfiscal import SpedFiscal

sped_fiscal = SpedFiscal()
sped_fiscal.importar_arquivo('/PATH')
```

### Registros Implementados

- [ ] Bloco C
  - [x] C001
  - [x] C100
  - [x] C170
  - [x] C190
  - [x] C195
  - [x] C197

### Instalação

- `pip install pyspedfiscal`

### Dependencias

- Pydantic
