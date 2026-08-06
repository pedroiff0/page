---
publish: true
title: Nota 01 - Algoritmos E Estruturas De Dados II
password: "engcomp20232"
---

# Nota 01

Conteúdo da sua anotação aqui.

## 🗺️ Tabela Dinâmica de Anotações (Quartz Base)

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/Engenharia de Computação/4-periodo/algoritmos-e-estruturas-de-dados-ii/anotacoes")'
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

