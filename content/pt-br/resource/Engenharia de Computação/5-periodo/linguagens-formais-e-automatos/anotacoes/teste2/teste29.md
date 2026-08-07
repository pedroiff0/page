---
publish: true
password: "eng232"
---

abcc
abbbbb
cccc
aabbcc
abc
bbbc
b
aaa
aaccc
bc
abc

## 📝 Anotações da Disciplina

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/Engenharia de Computação/5-periodo/linguagens-formais-e-automatos/anotacoes/teste2")'
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

