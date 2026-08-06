---
title: Anotações e Arquivos
publish: true
password: "engcomp20232"
---

## 📝 Base de Dados de Anotações

| Nome da Anotação | Acessar |
|------------------|---------|
| 📄 nota-01 | [[pt-br/resource/Engenharia de Computação/8-periodo/arquitetura-de-computadores/anotacoes/nota-01\|Acessar Anotação]] |

## 📎 Base de Dados de Arquivos

| Arquivo / Documento | Link de Acesso |
|---------------------|----------------|
| 📦 260423-Atividades.md | [Baixar / Ver Arquivo](/assets/disciplinas/8-periodo/arquitetura-de-computadores/260423-Atividades.md) |
| 📦 Introdução_à_Arquitetura_RISC_V.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/8-periodo/arquitetura-de-computadores/Introdu%C3%A7%C3%A3o_%C3%A0_Arquitetura_RISC_V.pdf) |
| 📦 Programação_Assembly_RISC_V.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/8-periodo/arquitetura-de-computadores/Programa%C3%A7%C3%A3o_Assembly_RISC_V.pdf) |


## 📝 Base Dinâmica de Anotações (Quartz Base)

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/Engenharia de Computação/8-periodo/arquitetura-de-computadores/anotacoes")'
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
