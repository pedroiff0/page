---
publish: true
title: "🌟 Lecture 02 — HR Diagram & Star Clusters"
titulo: CursoON-Aula02
disciplina: Galactic Archaeology and Stellar Populations (National Observatory)
conteudo: Open vs. globular clusters, the initial mass function (IMF), isochrones, and the population I/II/III nomenclature
professor: Hélio Dotto Perottoni
created: 2026-07-23
tags:
  - curso-on
  - galactic-archaeology
  - stellar-populations
  - star-clusters
cssclasses:
  - page-grid
  - center-images
---
# 🌟 Lecture 02 — HR Diagram & Star Clusters

> [!note] Summary
> Stars of different masses evolve differently — and that difference is exactly what makes star clusters ideal laboratories for testing stellar evolution models: every star in a cluster was (nearly) born at the same time. This lecture compares open and globular clusters, introduces the initial mass function (IMF) and isochrones, and closes with the population I/II/III nomenclature.

> [!info] Lecture info
> **Course:** Galactic Archaeology and Stellar Populations
> **Institution:** National Observatory (ON), Brazil
> **Professor:** Hélio Dotto Perottoni

---

## 📈 Why clusters?

On the HR diagram (Hipparcos 1997), solar-neighborhood stars appear with **all sorts of different ages and chemical compositions** — the Main Sequence, the giant branch, and other phases coexist mixed together. Because different masses evolve at different rates, and chemical composition also affects evolution, the distribution of a **cluster's** stars on the HR diagram essentially reflects the mass differences between them — since they all formed (approximately) together, with the same age and composition. A single cluster already contains stars at several evolutionary stages: main sequence, red giants, horizontal branch.

## 🔵🔴 Two basic types of clusters

| | Open clusters (e.g., Pleiades) | Globular clusters (e.g., ω Centauri) |
|---|---|---|
| Populations | Young | Old |
| Number of stars | $10^2$–$10^3$ | $10^4$–$10^6$ |
| Gravitational binding | Weak | Strong |
| Metallicity | Metal-rich | Metal-poor |
| Shape | Irregular | ~Spherical |
| Location | Galactic disk (spiral arms) | Halo / far from the plane |

### Open clusters

Characteristic visual properties: many blue stars, individually resolved stars (not as dense as globulars), no well-defined shape (hard to identify a center), and sometimes visible residual gas. They're made essentially of young stars — near-absence of evolved stars, extended main sequence — with hundreds to a few thousand weakly gravitationally-bound stars. Because they're not strongly bound, they're quickly destroyed by gravitational interactions with the rest of the Galaxy, so spatial coherence is only observed while they're young. Being young, they form from gas clouds that had time to be enriched with metals from previous generations — hence the high metallicity.

### Globular clusters

Dominated by old (redder) stars, occupying different evolutionary stages on the HR diagram — well-defined horizontal branch and red giant branch, with a characteristic apparent turnoff. Being old yet still spatially coherent implies they must be **strongly** gravitationally bound — consistent with the large density and star counts (tens of thousands to millions). Being old, their stars are typically metal-poor.

> [!tip] How do we know which stars really belong to a cluster?
> Today, one can combine proper motions and parallaxes measured by the **Gaia** mission with theoretical models of matching age/metallicity to determine membership probability — accepting, for example, only stars with >99.9% membership probability, yielding a "clean" HR diagram.

## 🧮 Initial Mass Function (IMF)

The **IMF** describes the probability that a star of a given mass will form in a given environment [Offner et al. 2014]. The distribution shows that the probability of forming high-mass stars ($>10\,M_\odot$) is very low in all observed cases.

> [!warning] Open questions about the IMF
> - How does the IMF behave in the limit of very high masses ($\sim100\,M_\odot$)?
> - What is the characteristic mass (the IMF's peak)?
> - Is the IMF **universal**, or does it vary across star-forming environments?
>
> The IMF's exact shape is crucial across many branches of Astronomy: the stellar mass distribution controls the evolution of a group of stars, and, for entire galaxies, the timescales for chemical enrichment, supernova occurrence, and interstellar medium dynamics.

Combining **stellar evolution theory** with the **IMF** makes it possible to build complete models for a cluster's simple stellar populations (SSPs).

## 📐 Simple stellar populations and isochrones

An **isochrone** is a curve on the HR diagram representing a population of simple stars — same age, same chemical composition.

> [!warning] Isochrone ≠ evolutionary track
> Isochrones depict **entire** stellar populations (all the stars of a cluster, at one instant), while evolutionary tracks describe the evolution of a **single star** over time. These are frequently confused, but orthogonal, concepts.

Four parameters shape an isochrone's form: **reddening**, **distance**, **age**, and **metallicity** [Souza et al. 2020] — the same four parameters that reappear in Lecture 07 as free parameters in the cluster-based distance fit.

Populations of the **same age** are the ideal environment for studying how stellar evolution depends on mass — comparing young and old populations side by side [Babusiaux et al. 2018].

## 🗺️ Clusters in the context of the Galaxy

Since open clusters host young populations, they must be tied to regions where gas is available to form stars: the **galactic plane**, especially the gas- and dust-rich spiral-arm disk. That's why open clusters are used to **map the disk and spiral arms** [Hao et al. 2021; Castro-Ginard et al. 2021] — the current reference catalog totals **5647 open clusters** [Hunt & Reffert 2024].

Globular clusters, being old, can occupy regions far from the galactic plane — in the halo.

## 🏷️ Stellar populations (I, II, and III)

- **Population I:** young and metal-rich. The most abundant type in the Galaxy; typical of open clusters and spiral arms. **The Sun is a Population I star.**
- **Population II:** old and metal-poor. Typical of globular clusters, the Galaxy's halo, and predominant in elliptical galaxies.
- **Population III:** hypothetical — the **first stars ever born in the Universe**, made only of H and He (+ traces of light elements), forming before any chemical enrichment. **No Population III star has ever been found** — the lowest metallicity ever observed is only $10^{-7}$ the Sun's proportion of heavy elements [Frebel & Norris 2018].

---

## 📌 Key concepts

- **Open vs. globular clusters:** young/metal-rich/disk vs. old/metal-poor/halo — the observational pair that anchors the simple stellar population concept.
- **IMF:** probability distribution of stellar masses at birth — still uncertain in the high-mass regime and regarding universality.
- **Isochrone:** an HR curve for an entire population of matching age/metallicity — not to be confused with an individual evolutionary track.
- **Pop I / II / III:** decreasing metallicity/increasing age nomenclature; Pop III never directly observed.

## 🔗 References and related

- Hunt & Reffert (2024) — catalog of 5647 open clusters
- Offner et al. (2014) — review of the initial mass function
- Souza et al. (2020) — parameters shaping isochrones
- Babusiaux et al. (2018) — young vs. old populations with Gaia data
- Frebel & Norris (2018) — search for Population III / extremely metal-poor stars
- Hao et al. (2021); Castro-Ginard et al. (2021) — disk mapping via open clusters
- [CursoON — overview](en/resource/curso-on)
- [Lecture 01 — Concept & History](en/resource/curso-on/aula-01-conceito-e-historico)
- [Lecture 03 — Magnitudes, Colors & Spectral Classification](en/resource/curso-on/aula-03-magnitudes-cores-e-classificacao-espectral)
- [Winter School — Star Clusters](pt-br/resource/escolainverno/aglomerados) — sibling minicourse on the same topic (Portuguese only)
