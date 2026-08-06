---
title: Anotações e Arquivos
publish: true
password: "engcomp20232"
---

## 📝 Base de Dados de Anotações

| Nome da Anotação | Acessar |
|------------------|---------|
| 📄 nota-01 | [[pt-br/resource/Engenharia de Computação/3-periodo/mecanica-dos-solidos/anotacoes/nota-01\|Acessar Anotação]] |

## 📎 Base de Dados de Arquivos

| Arquivo / Documento | Link de Acesso |
|---------------------|----------------|
| 📦 162061-Lista2.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/3-periodo/mecanica-dos-solidos/162061-Lista2.pdf) |
| 📦 163071-concurso-de-estruturas-apostila.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/3-periodo/mecanica-dos-solidos/163071-concurso-de-estruturas-apostila.pdf) |
| 📦 163981-Lista3.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/3-periodo/mecanica-dos-solidos/163981-Lista3.pdf) |
| 📦 164101-Lista4.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/3-periodo/mecanica-dos-solidos/164101-Lista4.pdf) |
| 📦 Relatório Mecânica dos Sólidos.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/3-periodo/mecanica-dos-solidos/Relat%C3%B3rio%20Mec%C3%A2nica%20dos%20S%C3%B3lidos.pdf) |
| 📦 exsMec.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/3-periodo/mecanica-dos-solidos/exsMec.pdf) |


## 📝 Base Dinâmica de Anotações (Quartz Base)

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/Engenharia de Computação/3-periodo/mecanica-dos-solidos/anotacoes")'
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
