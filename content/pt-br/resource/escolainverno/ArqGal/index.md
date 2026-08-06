---
publish: true
title: Arqueologia Galáctica
created: 2026-07-22
modified: 2026-07-26T11:03:14.091-03:00
published: 2026-07-26T11:03:14.091-03:00
---

> [!note] Resumo
> A história da Via Láctea lida na composição química e cinemática das estrelas.

<div class="media-carousel">
  <a href="/pt-br/resource/escolainverno/arqgal/arqueologiagalactica-aula01" class="carousel-slide">
    <img src="/assets/illustrations/arqgal.svg" alt="Aula 01" />
    <div class="slide-caption">Aula 01</div>
  </a>
  <a href="/pt-br/resource/escolainverno/arqgal/arqueologiagalactica-aula02" class="carousel-slide">
    <img src="/assets/illustrations/arqgal.svg" alt="Aula 02" />
    <div class="slide-caption">Aula 02</div>
  </a>
  <a href="/pt-br/resource/escolainverno/arqgal/arqueologiagalactica-aula03" class="carousel-slide">
    <img src="/assets/illustrations/arqgal.svg" alt="Aula 03" />
    <div class="slide-caption">Aula 03</div>
  </a>
</div>

A história da Via Láctea lida na composição química e cinemática das estrelas.


## 🗺️ Tabela Dinâmica do Minicurso (Quartz Base)

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/escolainverno/ArqGal")'
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
