---
publish: true
title: Computação de Alto Desempenho
created: 2026-07-22
modified: 2026-07-26T11:05:47.333-03:00
published: 2026-07-26T11:05:47.333-03:00
---

> [!note] Resumo
> Programação paralela (OpenMP/MPI) para ciência de dados, com Fernando Roig.

<div class="media-carousel">
  <a href="/pt-br/resource/escolainverno/computação/computacao-aula01" class="carousel-slide">
    <img src="/assets/illustrations/computacao.svg" alt="Aula 01" />
    <div class="slide-caption">Aula 01</div>
  </a>
  <a href="/pt-br/resource/escolainverno/computação/computacao-aula02" class="carousel-slide">
    <img src="/assets/illustrations/computacao.svg" alt="Aula 02" />
    <div class="slide-caption">Aula 02</div>
  </a>
  <a href="/pt-br/resource/escolainverno/computação/computacao-aula03" class="carousel-slide">
    <img src="/assets/illustrations/computacao.svg" alt="Aula 03" />
    <div class="slide-caption">Aula 03</div>
  </a>
</div>

Programação paralela (OpenMP/MPI) para ciência de dados, com Fernando Roig.

## 📚 Aulas

1. [Aula 01](pt-br/resource/escolainverno/computação/computacao-aula01) — fundamentos de Computação de Alto Desempenho (HPC): processos vs. threads, os dois modelos de memória, e paralelismo com OpenMP (memória compartilhada) e MPI (memória distribuída).
2. [Aula 02](pt-br/resource/escolainverno/computação/computacao-aula02) — duas partes: desempenho e arquitetura de MPI (continuação da Aula 01), e uma introdução a dados e aprendizado de máquina aplicados à astronomia.
3. [Aula 03](pt-br/resource/escolainverno/computação/computacao-aula03) — _(nota provisória, aguardando material oficial)_ panorama de algoritmos clássicos de aprendizado de máquina, supervisionados (regressão linear, árvores de decisão, random forest, k-NN) e não supervisionados (PCA, t-SNE, UMAP).


## 🗺️ Tabela Dinâmica do Minicurso (Quartz Base)

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/escolainverno/Computação")'
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
