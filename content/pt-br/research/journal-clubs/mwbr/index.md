---
publish: true
title: MWBR
created: 2026-07-26
modified: 2026-07-31
---

> [!note] Resumo
> Artigos discutidos no journal club do **MWBR**, grupo de pesquisa em Via Láctea, arqueologia galáctica e populações estelares. Ver o [padrão de cada entrada](pt-br/research/journal-clubs#padrão-de-cada-entrada).

A tabela abaixo é gerada a partir do frontmatter das próprias notas de artigo desta pasta — uma nota nova aparece sozinha no próximo build, sem editar esta página.

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/research/journal-clubs/mwbr")'
    - 'file.name != "index"'
formulas:
  artigo: 'link(file.path, note.title)'
  # A URL do arXiv entra como texto e o Quartz a transforma em link externo
  # sozinho. Não usar link() aqui: ele só resolve caminho interno e transforma
  # uma URL em "../../https/arxiv.org/...". html() também não serve — o markup
  # é escapado antes de chegar na célula.
properties:
  formula.artigo:
    displayName: Artigo
  note.authors:
    displayName: Autoria
  note.year:
    displayName: Ano
  note.discutido:
    displayName: Discutido em
  note.arxiv:
    displayName: arXiv
views:
  - type: table
    name: Artigos discutidos
    order:
      - formula.artigo
      - note.authors
      - note.year
      - note.discutido
      - note.arxiv
    sort:
      - property: note.discutido
        direction: DESC
```

_Nenhum artigo publicado ainda — em curadoria._ <!-- apagar esta linha quando a primeira nota de artigo entrar -->

---

## 🔗 Referências e correlatos

- [Journal Clubs — visão geral](pt-br/research/journal-clubs)
- [ENGCOMP](pt-br/research/journal-clubs/engcomp)
- [Pesquisa — visão geral](pt-br/research)
