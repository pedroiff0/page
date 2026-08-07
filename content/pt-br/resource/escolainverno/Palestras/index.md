---
publish: true
title: Palestras da Escola de Inverno
created: 2026-07-22
modified: 2026-08-06
published: 2026-07-26T10:42:30.234-03:00
---

> [!note] Resumo
> Ciclo de palestras da Escola de Inverno em Astrofísica 2026 do Observatório Nacional.

<div class="media-carousel">
  <a href="/pt-br/resource/escolainverno/palestras/neutrinos" class="carousel-slide">
    <img src="/assets/illustrations/palestras.svg" alt="Neutrinos" />
    <div class="slide-caption">Neutrinos</div>
  </a>
  <a href="/pt-br/resource/escolainverno/palestras/oasi" class="carousel-slide">
    <img src="/assets/illustrations/palestras.svg" alt="OASI" />
    <div class="slide-caption">OASI</div>
  </a>
  <a href="/pt-br/resource/escolainverno/palestras/raiox" class="carousel-slide">
    <img src="/assets/illustrations/palestras.svg" alt="Raio-X" />
    <div class="slide-caption">Raio-X</div>
  </a>
  <a href="/pt-br/resource/escolainverno/palestras/composicoes" class="carousel-slide">
    <img src="/assets/illustrations/palestras.svg" alt="Composições Químicas" />
    <div class="slide-caption">Composições Químicas</div>
  </a>
  <a href="/pt-br/resource/escolainverno/palestras/bolsas" class="carousel-slide">
    <img src="/assets/illustrations/palestras.svg" alt="Bolsas" />
    <div class="slide-caption">Sessão PG/PIBIC</div>
  </a>
</div>

---

## 🎙️ Relação das Palestras Ministradas

- ⚛️ **P1:** [Neutrinos e a Cosmologia](/pt-br/resource/escolainverno/palestras/neutrinos) — Gabriel Rodrigues
- 🔭 **P2:** [15 Anos do OASI](/pt-br/resource/escolainverno/palestras/oasi) — Daniela Lazzaro
- 💥 **P3:** [Raios-X e Enriquecimento Químico no Universo](/pt-br/resource/escolainverno/palestras/raiox) — Rebeca Batalha
- 🧪 **P4:** [Composições Químicas Estelares de Alta Precisão](/pt-br/resource/escolainverno/palestras/composicoes) — Marília Carlos
- 🎓 **PG/PIBIC:** [Sessão de Pós-Graduação e Bolsas](/pt-br/resource/escolainverno/palestras/bolsas) — Coordenação ON

---

## 🎙️ Palestras

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/escolainverno/Palestras")'
    - 'file.name != "index"'
formulas:
  palestra: 'link(file.path, note.title)'
properties:
  formula.palestra:
    displayName: Palestra / Documento
  note.created:
    displayName: Data
views:
  - type: table
    name: Acervo de Palestras da Escola de Inverno
    order:
      - formula.palestra
      - note.created
    sort:
      - property: file.name
        direction: ASC
```
