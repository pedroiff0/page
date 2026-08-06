---
publish: true
title: Escola de Inverno em Astrofísica (ON 2026)
created: 2026-07-22
modified: 2026-08-06
published: 2026-07-26T10:41:58.418-03:00
---

> [!note] Resumo Institucional
> Notas de aula e palestras da **Escola de Inverno em Astrofísica 2026** do **Observatório Nacional (ON)**, realizada de 20 a 24 de julho de 2026.

<div class="media-carousel">
  <a href="/pt-br/resource/escolainverno/escola-de-inverno" class="carousel-slide">
    <img src="/assets/illustrations/escolainverno.svg" alt="Resumo Geral" />
    <div class="slide-caption">Resumo Geral</div>
  </a>
  <a href="/pt-br/resource/escolainverno/aglomerados" class="carousel-slide">
    <img src="/assets/illustrations/aglomerados.svg" alt="Aglomerados de Galáxias" />
    <div class="slide-caption">Aglomerados de Galáxias</div>
  </a>
  <a href="/pt-br/resource/escolainverno/apresentacao" class="carousel-slide">
    <img src="/assets/illustrations/apresentacao.svg" alt="Apresentação de Pesquisa" />
    <div class="slide-caption">Apresentação de Pesquisa</div>
  </a>
  <a href="/pt-br/resource/escolainverno/arqgal" class="carousel-slide">
    <img src="/assets/illustrations/arqgal.svg" alt="Arqueologia Galáctica" />
    <div class="slide-caption">Arqueologia Galáctica</div>
  </a>
  <a href="/pt-br/resource/escolainverno/computação" class="carousel-slide">
    <img src="/assets/illustrations/escolainverno.svg" alt="Computação de Alto Desempenho" />
    <div class="slide-caption">Computação de Alto Desempenho</div>
  </a>
  <a href="/pt-br/resource/escolainverno/cosmologia" class="carousel-slide">
    <img src="/assets/illustrations/cosmologia.svg" alt="Cosmologia" />
    <div class="slide-caption">Cosmologia</div>
  </a>
  <a href="/pt-br/resource/escolainverno/palestras" class="carousel-slide">
    <img src="/assets/illustrations/palestras.svg" alt="Palestras" />
    <div class="slide-caption">Palestras</div>
  </a>
  <a href="/pt-br/resource/escolainverno/planetaria" class="carousel-slide">
    <img src="/assets/illustrations/planetaria.svg" alt="Ciências Planetárias" />
    <div class="slide-caption">Ciências Planetárias</div>
  </a>
</div>

---

## 🔬 Minicursos Oficiais

- 🌌 **[Aglomerados de Galáxias](/pt-br/resource/escolainverno/aglomerados)** — *Prof. Rogério Monteiro-Oliveira*
- 🏛️ **[Arqueologia Galáctica](/pt-br/resource/escolainverno/arqgal)** — *João Victor Sales Silva*
- 💻 **[Computação de Alto Desempenho](/pt-br/resource/escolainverno/computação)** — *Fernando Roig e Lilianne Nakazono*
- 🔭 **[Cosmologia](/pt-br/resource/escolainverno/cosmologia)** — *Carlos Bengaly*
- 🪐 **[Ciências Planetárias](/pt-br/resource/escolainverno/planetaria)** — *Filipe Monteiro e Gustavo Madeira*

---

## 🎙️ Ciclo de Palestras do Observatório Nacional

- ⚛️ **[P1 — Neutrinos e a Cosmologia](/pt-br/resource/escolainverno/palestras/neutrinos)** — *Gabriel Rodrigues*
- 🔭 **[P2 — 15 anos do OASI](/pt-br/resource/escolainverno/palestras/oasi)** — *Daniela Lazzaro*
- 💥 **[P3 — Raios-X, Supernovas e Enriquecimento Químico](/pt-br/resource/escolainverno/palestras/raiox)** — *Rebeca Batalha*
- 🧪 **[P4 — Composições Químicas Estelares de Alta Precisão](/pt-br/resource/escolainverno/palestras/composicoes)** — *Marília Carlos*
- 🎓 **[Sessão PG/PIBIC — Programas de Pós-Graduação e Bolsas](/pt-br/resource/escolainverno/palestras/bolsas)** — *Equipe ON*

---

## 🎤 Apresentação de Pesquisa Discente

- 📜 **[Unveiling the Solar Vicinity (t-SNE & GALAH DR4)](/pt-br/resource/escolainverno/apresentacao)** — *Notas de preparação para apresentação de pôster.*

---

## 🗺️ Tabela Dinâmica dos Minicursos e Conteúdos (Quartz Base)

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/escolainverno")'
    - 'file.name == "index"'
    - 'file.path != "pt-br/resource/escolainverno/index.md"'
formulas:
  secao: 'link(file.path, note.title)'
properties:
  formula.secao:
    displayName: Módulo / Minicurso / Palestras
views:
  - type: table
    name: Módulos da Escola de Inverno 2026
    order:
      - formula.secao
    sort:
      - property: file.path
        direction: ASC
```

---

Programação oficial completa no [site do Observatório Nacional](https://www.gov.br/observatorio/pt-br/assuntos/areas-de-atuacao/astronomia-e-astrofisica/ensino/escola-de-inverno-em-astrofisica/2026).
