---
title: Anotações e Arquivos
publish: true
password: "engcomp20232"
---

## 📝 Base de Dados de Anotações

| Nome da Anotação | Acessar |
|------------------|---------|
| 📄 nota-01 | [[pt-br/resource/Engenharia de Computação/6-periodo/filosofia-da-ciencia-e-tecnologia/anotacoes/nota-01\|Acessar Anotação]] |

## 📎 Base de Dados de Arquivos

Nenhum arquivo encontrado.


## 📝 Base Dinâmica de Anotações (Quartz Base)

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/Engenharia de Computação/6-periodo/filosofia-da-ciencia-e-tecnologia/anotacoes")'
    - 'note.publish'
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
