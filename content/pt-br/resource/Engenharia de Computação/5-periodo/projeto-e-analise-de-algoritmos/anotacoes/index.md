---
title: Anotações e Arquivos
publish: true
password: "engcomp20232"
---

## 📝 Base de Dados de Anotações

| Nome da Anotação | Acessar |
|------------------|---------|
| 📄 260413-Aula-AtividadesAbril-1 | [[pt-br/resource/Engenharia de Computação/5-periodo/projeto-e-analise-de-algoritmos/anotacoes/260413-Aula-AtividadesAbril-1\|Acessar Anotação]] |
| 📄 260611-Comparação | [[pt-br/resource/Engenharia de Computação/5-periodo/projeto-e-analise-de-algoritmos/anotacoes/260611-Comparação\|Acessar Anotação]] |
| 📄 260618-RevisaoProva | [[pt-br/resource/Engenharia de Computação/5-periodo/projeto-e-analise-de-algoritmos/anotacoes/260618-RevisaoProva\|Acessar Anotação]] |
| 📄 nota-01 | [[pt-br/resource/Engenharia de Computação/5-periodo/projeto-e-analise-de-algoritmos/anotacoes/nota-01\|Acessar Anotação]] |

## 📎 Base de Dados de Arquivos

| Arquivo / Documento | Link de Acesso |
|---------------------|----------------|
| 📦 AtividadeAPA2025.2-2.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/5-periodo/projeto-e-analise-de-algoritmos/AtividadeAPA2025.2-2.pdf) |
| 📦 AtividadeAPA2025.2.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/5-periodo/projeto-e-analise-de-algoritmos/AtividadeAPA2025.2.pdf) |
| 📦 AtividadesPAA.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/5-periodo/projeto-e-analise-de-algoritmos/AtividadesPAA.pdf) |
| 📦 Atividades_PAA_Questoes_Objetivas.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/5-periodo/projeto-e-analise-de-algoritmos/Atividades_PAA_Questoes_Objetivas.pdf) |
| 📦 PAA-Aula2-OrdenaçãoExternaTeorica(02-04).pdf | [Baixar / Ver Arquivo](/assets/disciplinas/5-periodo/projeto-e-analise-de-algoritmos/PAA-Aula2-Ordena%C3%A7%C3%A3oExternaTeorica%2802-04%29.pdf) |
| 📦 PAA-Aula3-OrdenaçãoExternaPratica(09-04).pdf | [Baixar / Ver Arquivo](/assets/disciplinas/5-periodo/projeto-e-analise-de-algoritmos/PAA-Aula3-Ordena%C3%A7%C3%A3oExternaPratica%2809-04%29.pdf) |
| 📦 PAA-Aula3-OrdenaçãoExternaPratica.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/5-periodo/projeto-e-analise-de-algoritmos/PAA-Aula3-Ordena%C3%A7%C3%A3oExternaPratica.pdf) |
| 📦 PAA-Aula4-TabelaHAsh(16-04).pdf | [Baixar / Ver Arquivo](/assets/disciplinas/5-periodo/projeto-e-analise-de-algoritmos/PAA-Aula4-TabelaHAsh%2816-04%29.pdf) |
| 📦 PAA5EC-parte1 (6).pdf | [Baixar / Ver Arquivo](/assets/disciplinas/5-periodo/projeto-e-analise-de-algoritmos/PAA5EC-parte1%20%286%29.pdf) |
| 📦 PAA5EC-parte1-complexidade.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/5-periodo/projeto-e-analise-de-algoritmos/PAA5EC-parte1-complexidade.pdf) |
| 📦 PAA5EC-parte1.3 (1).pdf | [Baixar / Ver Arquivo](/assets/disciplinas/5-periodo/projeto-e-analise-de-algoritmos/PAA5EC-parte1.3%20%281%29.pdf) |
| 📦 PAA5EC-parte2-algoritmos.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/5-periodo/projeto-e-analise-de-algoritmos/PAA5EC-parte2-algoritmos.pdf) |
| 📦 PAA5EC-parte3-grafos.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/5-periodo/projeto-e-analise-de-algoritmos/PAA5EC-parte3-grafos.pdf) |
| 📦 PAA5EC-parte4-Classes de problemas.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/5-periodo/projeto-e-analise-de-algoritmos/PAA5EC-parte4-Classes%20de%20problemas.pdf) |
| 📦 PedroH_5EC_PAA_Atividades.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/5-periodo/projeto-e-analise-de-algoritmos/PedroH_5EC_PAA_Atividades.pdf) |
| 📦 PedroH_5EC_PAA_Rascunho.pdf | [Baixar / Ver Arquivo](/assets/disciplinas/5-periodo/projeto-e-analise-de-algoritmos/PedroH_5EC_PAA_Rascunho.pdf) |
| 📦 RevisãoOrdenação Externa(26-03).pdf | [Baixar / Ver Arquivo](/assets/disciplinas/5-periodo/projeto-e-analise-de-algoritmos/Revis%C3%A3oOrdena%C3%A7%C3%A3o%20Externa%2826-03%29.pdf) |
| 📦 RevisãoTabela Hash (26-03).pdf | [Baixar / Ver Arquivo](/assets/disciplinas/5-periodo/projeto-e-analise-de-algoritmos/Revis%C3%A3oTabela%20Hash%20%2826-03%29.pdf) |


## 📝 Base Dinâmica de Anotações (Quartz Base)

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/Engenharia de Computação/5-periodo/projeto-e-analise-de-algoritmos/anotacoes")'
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
