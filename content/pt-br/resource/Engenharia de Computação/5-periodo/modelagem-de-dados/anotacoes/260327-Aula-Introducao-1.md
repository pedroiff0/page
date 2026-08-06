---
publish: true
password: "engcomp20232"
titulo: 260327-Aula-Introducao-1
disciplina:
conteudo:
professor:
criado: sexta-feira 27/03/2026 21:27
modificado: sexta-feira 27/03/2026 21:27
tags:
cssclasses:
  - embed-manila
  - page-grid
  - recolor-images
  - center-images
---
# Notas de Aula - Introducao
***
## Entidades

## Dicionarização das Entidades do Modelo

## Atributos


***

> [!NOTE] Atenção:


***

## 🗺️ Tabela Dinâmica de Anotações (Quartz Base)

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/Engenharia de Computação/5-periodo/modelagem-de-dados/anotacoes")'
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

