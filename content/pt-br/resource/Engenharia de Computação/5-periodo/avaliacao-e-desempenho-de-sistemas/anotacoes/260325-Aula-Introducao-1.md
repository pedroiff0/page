---
publish: true
password: "eng232"
titulo: 260325-Aula-Introducao-1
disciplina:
conteudo:
professor:
criado: quarta-feira 25/03/2026 11:17
modificado: quarta-feira 25/03/2026 11:17
tags:
cssclasses:
  - embed-manila
  - page-grid
  - recolor-images
  - center-images
---
# Notas de Aula - Introducao
***
## Anotações
***

## Teoria de Filas

Sistemas de Fluxos

Processos Estocásticos

Notação de Kendall

Lei de Little


> [!NOTE] Atenção: KK
>


***

## 📝 Anotações da Disciplina

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/Engenharia de Computação/5-periodo/avaliacao-e-desempenho-de-sistemas/anotacoes")'
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

