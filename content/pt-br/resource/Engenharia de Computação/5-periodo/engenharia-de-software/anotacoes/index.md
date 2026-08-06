---
title: Anotações e Arquivos
publish: true
password: "engcomp20232"
---

## 📝 Base de Dados de Anotações

| Nome da Anotação | Acessar |
|------------------|---------|
| 📄 260326-Aula-Intro-1 | [[pt-br/resource/Engenharia de Computação/5-periodo/engenharia-de-software/anotacoes/260326-Aula-Intro-1\|Acessar Anotação]] |
| 📄 nota-01 | [[pt-br/resource/Engenharia de Computação/5-periodo/engenharia-de-software/anotacoes/nota-01\|Acessar Anotação]] |

## 📎 Base de Dados de Arquivos

| Arquivo / Documento | Link de Acesso |
|---------------------|----------------|
| 📦 Exercicio Proposto Resolvido - Engenharia de Software.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/5-periodo/engenharia-de-software/Exercicio%20Proposto%20Resolvido%20-%20Engenharia%20de%20Software.pdf) |
| 📦 Exercicios Engenharia de Software.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/5-periodo/engenharia-de-software/Exercicios%20Engenharia%20de%20Software.pdf) |


## 📝 Base Dinâmica de Anotações (Quartz Base)

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/Engenharia de Computação/5-periodo/engenharia-de-software/anotacoes")'
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
