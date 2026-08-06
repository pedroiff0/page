---
publish: true
title: Apresentação de Pesquisa
created: 2026-07-22
modified: 2026-07-26T11:03:55.936-03:00
published: 2026-07-26T11:03:55.936-03:00
---

> [!note] Resumo
> Notas de preparação para a apresentação da minha pesquisa, reunindo o Banner SBPC 2026 e o Banner da Escola de Inverno.

<div class="media-carousel">
  <a href="/pt-br/resource/escolainverno/apresentacao/minhapesquisa-vizinhancasolar-tsne" class="carousel-slide">
    <img src="/assets/illustrations/apresentacao.svg" alt="Vizinhança Solar com t-SNE" />
    <div class="slide-caption">Vizinhança Solar com t-SNE</div>
  </a>
</div>

Notas de preparação para a apresentação da minha pesquisa


## 🗺️ Tabela Dinâmica do Minicurso (Quartz Base)

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/escolainverno/Apresentacao")'
    - 'file.name != "index"'
formulas:
  aula: 'link(file.path, note.title)'
properties:
  formula.aula:
    displayName: Aula / Conteúdo
  note.created:
    displayName: Data
views:
  - type: table
    name: Aulas do Minicurso
    order:
      - formula.aula
      - note.created
    sort:
      - property: file.name
        direction: ASC
```
