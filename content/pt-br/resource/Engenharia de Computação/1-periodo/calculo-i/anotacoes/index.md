---
title: Anotações e Arquivos
publish: true
password: "engcomp20232"
---

## 📝 Base de Dados de Anotações

| Nome da Anotação | Acessar |
|------------------|---------|
| 📄 nota-01 | [[pt-br/resource/Engenharia de Computação/1-periodo/calculo-i/anotacoes/nota-01\|Acessar Anotação]] |

## 📎 Base de Dados de Arquivos

| Arquivo / Documento | Link de Acesso |
|---------------------|----------------|
| 📦 Calculo.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/1-periodo/calculo-i/Calculo.pdf) |
| 📦 Desafio 2.ggb | [Baixar / Ver Arquivo](/assets/disciplinas/1-periodo/calculo-i/Desafio%202.ggb) |
| 📦 Desafio.ggb | [Baixar / Ver Arquivo](/assets/disciplinas/1-periodo/calculo-i/Desafio.ggb) |
| 📦 GraficosGeoGebra 2.ggb | [Baixar / Ver Arquivo](/assets/disciplinas/1-periodo/calculo-i/GraficosGeoGebra%202.ggb) |
| 📦 GraficosGeoGebra.ggb | [Baixar / Ver Arquivo](/assets/disciplinas/1-periodo/calculo-i/GraficosGeoGebra.ggb) |
| 📦 LISTA DE EXERCÍCIOS 1 (1)_230926_180312_230926_180425 2.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/1-periodo/calculo-i/LISTA%20DE%20EXERC%C3%8DCIOS%201%20%281%29_230926_180312_230926_180425%202.pdf) |
| 📦 LISTA DE EXERCÍCIOS 1 (1)_230926_180312_230926_180425.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/1-periodo/calculo-i/LISTA%20DE%20EXERC%C3%8DCIOS%201%20%281%29_230926_180312_230926_180425.pdf) |
| 📦 LISTA DE EXERCÍCIOS 2_231017_182527 2.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/1-periodo/calculo-i/LISTA%20DE%20EXERC%C3%8DCIOS%202_231017_182527%202.pdf) |
| 📦 LISTA DE EXERCÍCIOS 2_231017_182527.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/1-periodo/calculo-i/LISTA%20DE%20EXERC%C3%8DCIOS%202_231017_182527.pdf) |
| 📦 Lista Sugestão Funções .pdf | [Baixar / Ver Arquivo](/assets/disciplinas/1-periodo/calculo-i/Lista%20Sugest%C3%A3o%20Fun%C3%A7%C3%B5es%20.pdf) |
| 📦 Lista Sugestão Funções.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/1-periodo/calculo-i/Lista%20Sugest%C3%A3o%20Fun%C3%A7%C3%B5es.pdf) |
| 📦 Resumo 2.odt | [Baixar / Ver Arquivo](/assets/disciplinas/1-periodo/calculo-i/Resumo%202.odt) |
| 📦 Resumo.odt | [Baixar / Ver Arquivo](/assets/disciplinas/1-periodo/calculo-i/Resumo.odt) |
| 📦 atividadesDerivadas.ggb | [Baixar / Ver Arquivo](/assets/disciplinas/1-periodo/calculo-i/atividadesDerivadas.ggb) |


## 📝 Base Dinâmica de Anotações (Quartz Base)

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/Engenharia de Computação/1-periodo/calculo-i/anotacoes")'
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
