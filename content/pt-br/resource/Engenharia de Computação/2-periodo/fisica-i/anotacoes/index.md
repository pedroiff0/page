---
title: Anotações e Arquivos
publish: true
password: "engcomp20232"
---

## 📝 Base de Dados de Anotações

| Nome da Anotação | Acessar |
|------------------|---------|
| 📄 nota-01 | [[pt-br/resource/Engenharia de Computação/2-periodo/fisica-i/anotacoes/nota-01\|Acessar Anotação]] |

## 📎 Base de Dados de Arquivos

| Arquivo / Documento | Link de Acesso |
|---------------------|----------------|
| 📦 154731-Lista_de_Exercícios_de_Física_I_Eng_Comp.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/2-periodo/fisica-i/154731-Lista_de_Exerc%C3%ADcios_de_F%C3%ADsica_I_Eng_Comp.pdf) |
| 📦 155581-2°_Lista_de_Exercícios_de_Física_I_Eng._Comp_(1).pdf | [Baixar / Ver Arquivo](/assets/disciplinas/2-periodo/fisica-i/155581-2%C2%B0_Lista_de_Exerc%C3%ADcios_de_F%C3%ADsica_I_Eng._Comp_%281%29.pdf) |
| 📦 157001-3°_Lista_de_Exercícios_de_Física_I_Eng._Comp._-_Copiar.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/2-periodo/fisica-i/157001-3%C2%B0_Lista_de_Exerc%C3%ADcios_de_F%C3%ADsica_I_Eng._Comp._-_Copiar.pdf) |
| 📦 157981-4°_Lista_Eng._Computação.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/2-periodo/fisica-i/157981-4%C2%B0_Lista_Eng._Computa%C3%A7%C3%A3o.pdf) |
| 📦 Caderno Física I (1).pdf | [Baixar / Ver Arquivo](/assets/disciplinas/2-periodo/fisica-i/Caderno%20F%C3%ADsica%20I%20%281%29.pdf) |
| 📦 Caderno Física I.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/2-periodo/fisica-i/Caderno%20F%C3%ADsica%20I.pdf) |
| 📦 correcaoprova1.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/2-periodo/fisica-i/correcaoprova1.pdf) |
| 📦 fisica-1-2.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/2-periodo/fisica-i/fisica-1-2.pdf) |
| 📦 gabaritolista1.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/2-periodo/fisica-i/gabaritolista1.pdf) |
| 📦 gabaritolista2.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/2-periodo/fisica-i/gabaritolista2.pdf) |
| 📦 lista-2.1.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/2-periodo/fisica-i/lista-2.1.pdf) |


## 📝 Base Dinâmica de Anotações (Quartz Base)

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/Engenharia de Computação/2-periodo/fisica-i/anotacoes")'
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
