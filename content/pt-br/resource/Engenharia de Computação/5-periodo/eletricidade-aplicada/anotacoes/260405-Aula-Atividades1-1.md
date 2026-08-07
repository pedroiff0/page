---
publish: true
password: "eng232"
titulo: 260405-Aula-Atividades1-1
disciplina:
conteudo:
professor:
criado: domingo 05/04/2026 21:48
modificado: domingo 05/04/2026 21:48
tags:
cssclasses:
---
# Notas de Aula - Atividades1
***
## Anotações
***
Lista de Atividades, Cap. 9 - Alexander:

9.2: 1, 2, 3, 4
9.3: 11, 16, 18, 19
9.4: 27, 28, 29, 31, 33
9.5: 35, 40, 47
9.7: 53,  56

## Fórmulas para prova:



> [!NOTE] Atenção:


***

## 📝 Anotações da Disciplina

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

