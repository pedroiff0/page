---
publish: true
password: "engcomp20232"
titulo:  260611-Comparação
disciplina:
conteudo:
professor:
criado: quinta-feira 11/06/2026 17:17
modificado: quinta-feira 11/06/2026 17:17
tags:
cssclasses:
  - page-grid
  - center-images

---
# Notas de Aula - Comparação
***
## Anotações
***

$$T_1(n) = n^2 - 600n + 150000$$
$$T_2(n) = 2n^2 - 1200n + 200000$$
1. Para que tamanho da entrada T1 é mais rápido que T2? 
2. Para que tamanho da entrada T2 é mais rápido que T1?
3. Para que tamanho da entrada os dois executam em tempos iguais?
$$T_1 = T_2$$
$$n^2 - 600n + 150000 = T_2$$

***

## 🗺️ Tabela Dinâmica de Anotações (Quartz Base)

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/Engenharia de Computação/5-periodo/projeto-e-analise-de-algoritmos/anotacoes")'
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

