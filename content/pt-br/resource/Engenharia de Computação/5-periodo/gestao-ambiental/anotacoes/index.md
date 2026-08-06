---
title: Anotações e Arquivos
publish: true
password: "engcomp20232"
---

## 📝 Base de Dados de Anotações

| Nome da Anotação | Acessar |
|------------------|---------|
| 📄 260326-Aula-Intro-1 | [[pt-br/resource/Engenharia de Computação/5-periodo/gestao-ambiental/anotacoes/260326-Aula-Intro-1\|Acessar Anotação]] |
| 📄 260406-Aula-Pesquisa-1 | [[pt-br/resource/Engenharia de Computação/5-periodo/gestao-ambiental/anotacoes/260406-Aula-Pesquisa-1\|Acessar Anotação]] |
| 📄 260409-Aula-PegadaAmbiental-1 | [[pt-br/resource/Engenharia de Computação/5-periodo/gestao-ambiental/anotacoes/260409-Aula-PegadaAmbiental-1\|Acessar Anotação]] |
| 📄 nota-01 | [[pt-br/resource/Engenharia de Computação/5-periodo/gestao-ambiental/anotacoes/nota-01\|Acessar Anotação]] |

## 📎 Base de Dados de Arquivos

| Arquivo / Documento | Link de Acesso |
|---------------------|----------------|
| 📦 Gestao_Ambiental_Apostila_Completa_00582.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/5-periodo/gestao-ambiental/Gestao_Ambiental_Apostila_Completa_00582.pdf) |
| 📦 Meio Ambiente e Gestão Ambiental.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/5-periodo/gestao-ambiental/Meio%20Ambiente%20e%20Gest%C3%A3o%20Ambiental.pdf) |
| 📦 NBR-ISO-14.001-Sistemas-de-Gestão-Ambiental.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/5-periodo/gestao-ambiental/NBR-ISO-14.001-Sistemas-de-Gest%C3%A3o-Ambiental.pdf) |
| 📦 introducao_SG.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/5-periodo/gestao-ambiental/introducao_SG.pdf) |


## 📝 Base Dinâmica de Anotações (Quartz Base)

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/Engenharia de Computação/5-periodo/gestao-ambiental/anotacoes")'
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
