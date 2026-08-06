---
publish: true
title: Aglomerados de Galáxias
created: 2026-07-22
modified: 2026-07-26T10:53:56.976-03:00
published: 2026-07-26T10:53:56.976-03:00
---

> [!note] Resumo
> Aglomerados de galáxias: as maiores estruturas gravitacionalmente ligadas do Universo, com [Rogério Monteiro-Oliveira](https://www.monteiro-oliveira.com).

<div class="media-carousel">
  <a href="/pt-br/resource/escolainverno/aglomerados/aglomerados-aula01" class="carousel-slide">
    <img src="/assets/illustrations/aglomerados.svg" alt="Aula 01" />
    <div class="slide-caption">Aula 01</div>
  </a>
  <a href="/pt-br/resource/escolainverno/aglomerados/aglomerados-aula02" class="carousel-slide">
    <img src="/assets/illustrations/aglomerados.svg" alt="Aula 02" />
    <div class="slide-caption">Aula 02</div>
  </a>
  <a href="/pt-br/resource/escolainverno/aglomerados/aglomerados-aula03" class="carousel-slide">
    <img src="/assets/illustrations/aglomerados.svg" alt="Aula 03" />
    <div class="slide-caption">Aula 03</div>
  </a>
</div>

Aglomerados de galáxias: as maiores estruturas gravitacionalmente ligadas do Universo, com [Rogério Monteiro-Oliveira](https://www.monteiro-oliveira.com).

## 📚 Aulas

1. [Aula 01](pt-br/resource/escolainverno/aglomerados/aglomerados-aula01) — o que é um aglomerado: escalas do cosmos, a "receita" física (matéria escura, gás intra-aglomerado, galáxias), e como detectá-los observacionalmente.
2. [Aula 02](pt-br/resource/escolainverno/aglomerados/aglomerados-aula02) — formação hierárquica a partir de flutuações de densidade primordiais, e os mecanismos que "matam" a formação estelar das galáxias ao caírem no aglomerado — terminando na BCG, a galáxia mais extrema desse processo.
3. [Aula 03](pt-br/resource/escolainverno/aglomerados/aglomerados-aula03) — o formalismo de lentes gravitacionais fracas, e como aglomerados em fusão (como o Aglomerado Bala) funcionam como laboratórios para testar se a matéria escura interage consigo mesma (SIDM).


## 🗺️ Tabela Dinâmica do Minicurso (Quartz Base)

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/escolainverno/Aglomerados")'
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
