---
publish: true
password: "engcomp20232"
titulo:  260406-Aula-Pesquisa-1
disciplina:
conteudo:
professor:
criado: segunda-feira 06/04/2026 23:02
modificado: segunda-feira 06/04/2026 23:02
tags:
cssclasses:
  - page-grid
  - center-images

---
# Notas de Aula - Pesquisa
***
## Anotações
***


> [!NOTE] Atenção:


***

## 🗺️ Tabela Dinâmica de Anotações (Quartz Base)

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/Engenharia de Computação/5-periodo/gestao-ambiental/anotacoes")'
    - 'file.ext == "md"'
    - 'file.name != "index"'
formulas:
  anotacao: 'link(file.path, note.title)'
properties:
  formula.anotacao:
    displayName: Anotação / Documento
  note.created:
    displayName: Data de Criação
views:
  - type: table
    name: Anotações da Disciplina
    order:
      - formula.anotacao
      - note.created
    sort:
      - property: file.name
        direction: ASC
```

