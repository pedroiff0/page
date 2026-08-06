---
title: Anotações e Arquivos
publish: true
password: "engcomp20232"
---

## 📝 Base de Dados de Anotações

| Nome da Anotação | Acessar |
|------------------|---------|
| 📄 nota-01 | [[pt-br/resource/Engenharia de Computação/2-periodo/algebra-linear-e-geometria-analitica-ii/anotacoes/nota-01\|Acessar Anotação]] |

## 📎 Base de Dados de Arquivos

| Arquivo / Documento | Link de Acesso |
|---------------------|----------------|
| 📦 152113-ALGA_II.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/2-periodo/algebra-linear-e-geometria-analitica-ii/152113-ALGA_II.pdf) |
| 📦 152114-Apresentação_2.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/2-periodo/algebra-linear-e-geometria-analitica-ii/152114-Apresenta%C3%A7%C3%A3o_2.pdf) |
| 📦 152115-Apresentação_3.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/2-periodo/algebra-linear-e-geometria-analitica-ii/152115-Apresenta%C3%A7%C3%A3o_3.pdf) |
| 📦 153042-Trabalho_1.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/2-periodo/algebra-linear-e-geometria-analitica-ii/153042-Trabalho_1.pdf) |
| 📦 155101-Lista_1.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/2-periodo/algebra-linear-e-geometria-analitica-ii/155101-Lista_1.pdf) |
| 📦 155571-Trabalho_ALGA_II.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/2-periodo/algebra-linear-e-geometria-analitica-ii/155571-Trabalho_ALGA_II.pdf) |
| 📦 155572-Trabalho_ALGA_II_-_Respostas.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/2-periodo/algebra-linear-e-geometria-analitica-ii/155572-Trabalho_ALGA_II_-_Respostas.pdf) |
| 📦 157571-Lista_2.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/2-periodo/algebra-linear-e-geometria-analitica-ii/157571-Lista_2.pdf) |
| 📦 157572-Lista_2_-_Respostas.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/2-periodo/algebra-linear-e-geometria-analitica-ii/157572-Lista_2_-_Respostas.pdf) |
| 📦 TrabalhoAlgebraII.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/2-periodo/algebra-linear-e-geometria-analitica-ii/TrabalhoAlgebraII.pdf) |


## 📝 Base Dinâmica de Anotações (Quartz Base)

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/Engenharia de Computação/2-periodo/algebra-linear-e-geometria-analitica-ii/anotacoes")'
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
