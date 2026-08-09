---
publish: true
title: Ciências Planetárias
created: 2026-07-22
modified: 2026-07-26T11:06:05.943-03:00
published: 2026-07-26T11:06:05.943-03:00
---

> [!note] Resumo
> Sistema Solar: inventário, arquitetura e dinâmica orbital.

<div class="media-carousel">
  <a href="/pt-br/resource/escolainverno/planetaria/planetaria-aula01" class="carousel-slide">
    <img src="/assets/illustrations/planetaria.svg" alt="Aula 01" />
    <div class="slide-caption">Aula 01</div>
  </a>
  <a href="/pt-br/resource/escolainverno/planetaria/planetaria-aula02" class="carousel-slide">
    <img src="/assets/illustrations/planetaria.svg" alt="Aula 02" />
    <div class="slide-caption">Aula 02</div>
  </a>
  <a href="/pt-br/resource/escolainverno/planetaria/planetaria-aula03" class="carousel-slide">
    <img src="/assets/illustrations/planetaria.svg" alt="Aula 03" />
    <div class="slide-caption">Aula 03</div>
  </a>
</div>

Sistema Solar: inventário, arquitetura e dinâmica orbital.

## 📚 Aulas

1. [Aula 01](/pt-br/resource/escolainverno/planetaria/planetaria-aula01) — o Sistema Solar em perspectiva: inventário de corpos, arquitetura orbital, dinâmica e uma visão geral de como o Sistema Solar se formou.
2. [Aula 02](/pt-br/resource/escolainverno/planetaria/planetaria-aula02) — pequenos corpos do Sistema Solar (asteroides, cometas, objetos transnetunianos) e o que sua distribuição orbital revela sobre os modelos de formação — incluindo asteroides próximos da Terra (NEOs).
3. [Aula 03](/pt-br/resource/escolainverno/planetaria/planetaria-aula03) — _(nota provisória, tema ainda não confirmado)_ palpite mínimo de continuação rumo a exoplanetas e planetologia comparada.


## 🗺️ Aulas do Minicurso

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/escolainverno/Planetaria")'
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
