---
publish: true
password: "engcomp20232"
titulo:  260413-Aula-ProvaCap9-1
disciplina:
conteudo:
professor:
criado: segunda-feira 13/04/2026 09:40
modificado: segunda-feira 13/04/2026 09:40
tags:
cssclasses:
  - page-grid
  - center-images

---
# Notas de Aula - ProvaCap9
***
## Anotações
***

## Questão 1



> [!NOTE] Atenção:


***

## 🗺️ Tabela Dinâmica de Anotações (Quartz Base)

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/Engenharia de Computação/5-periodo/eletricidade-aplicada/anotacoes")'
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

