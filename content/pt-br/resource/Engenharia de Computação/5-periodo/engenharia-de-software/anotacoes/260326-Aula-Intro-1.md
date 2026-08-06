---
publish: true
password: "engcomp20232"
titulo: 260326-Aula-Intro-1
disciplina:
conteudo:
professor:
criado: quinta-feira 26/03/2026 10:44
modificado: quinta-feira 26/03/2026 10:44
tags:
cssclasses:
  - embed-manila
  - page-grid
  - recolor-images
  - center-images
  - pen-purple
---
# Notas de Aula - Intro
***
## Anotações
***
[EngSoft](https://engsoftmoderna.info)
[https://github.com/mtov/ESM-ExemplosCodigo](https://github.com/mtov/ESM-ExemplosCodigo)

> [!NOTE] Atenção:


***

## 🗺️ Tabela Dinâmica de Anotações (Quartz Base)

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/Engenharia de Computação/5-periodo/engenharia-de-software/anotacoes")'
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

