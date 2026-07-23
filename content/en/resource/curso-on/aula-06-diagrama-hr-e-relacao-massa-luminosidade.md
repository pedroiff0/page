---
publish: true
title: "📊 Lecture 06 — HR Diagram & Mass-Luminosity Relation"
titulo: CursoON-Aula06
disciplina: Galactic Archaeology and Stellar Populations (National Observatory)
conteudo: How to measure the fundamental physical properties of stars, and how the HR diagram reveals the relation between mass, luminosity, and lifetime
professor: Hélio Dotto Perottoni
created: 2026-07-23
tags:
  - curso-on
  - galactic-archaeology
  - stellar-populations
  - hr-diagram
cssclasses:
  - page-grid
  - center-images
---
# 📊 Lecture 06 — HR Diagram & Mass-Luminosity Relation

> [!note] Summary
> Mass, chemical composition, and age are the three fundamental properties that control a star's entire evolution — and the HR diagram is the central tool for reading them indirectly. This lecture closes the cycle started in Lecture 02, showing how to measure each stellar physical property and why the mass-luminosity relation explains why massive stars live shorter lives.

> [!info] Lecture info
> **Course:** Galactic Archaeology and Stellar Populations
> **Institution:** National Observatory (ON), Brazil
> **Professor:** Hélio Dotto Perottoni

---

## 🧬 Intrinsic stellar properties

Three fundamental properties control a star's evolution: **mass**, **chemical composition**, and **age**. From these, the observable physical properties derive: temperature/color, luminosity, surface gravity, radius, rotation, binarity, and stellar winds. A star's position on the HR diagram depends on all of these combined.

### How each property is measured

| Property | How it's measured |
|---|---|
| Effective temperature | Color indices; spectral line intensity |
| Luminosity | Flux + absolute magnitude (requires distance) |
| Radius | Combining $T$ and $L$ via the **Stefan-Boltzmann Law**: $L = 4\pi R^2 \sigma T^4$ |
| Surface gravity | Equivalent width of spectral lines (indirectly reveals radius, hence luminosity) |
| Chemical composition | Presence and intensity of spectral lines |
| Mass | Binary systems + Kepler's Laws (requires distance, to convert angular measurements into positions/velocities) |
| Age | Theoretical models (isochrones, Lecture 02) |

## 📈 The Hertzsprung-Russell diagram

The **HR Diagram** organizes stars by temperature/color (x-axis, decreasing) vs. luminosity/absolute magnitude (y-axis) [Russell 1914]. It was a monumental effort by many astronomers: luminosity can only be known if the distance is measured. The evolution of the data is dramatic:

- **Russell (1914):** original HR diagram, few stars.
- **Hipparcos (1997):** ~50,000 stars with parallax-measured distances.
- **Gaia (2018–):** ~50 million stars (and growing) — colors indicate point density.

### Regions of the diagram

- **Main Sequence (MS):** where stars produce energy by fusing H into He in the core (proton-proton chain). It's a **sequence of masses**: stars spend most of their lives here, so most observed stars are on the MS.
  - High mass ($M > \sim8\,M_\odot$): hotter, bluer, smaller $B-V$, more luminous ($L\propto T^4$) — evolve off the MS **quickly**.
  - Low mass ($M < \sim4\,M_\odot$): cooler, redder, larger $B-V$, less luminous — spend **more** time on the MS.
  - Intermediate mass: $4\,M_\odot < M < 8\,M_\odot$.
- **Subgiants:** transition phase between MS and red giant.
- **Red giants:** inert core (H exhausted), still burning H in a shell around the core — cooler than same-mass MS stars, but more luminous (much larger radii).
- **Horizontal branch:** stars produce energy in the core again, now by fusing He into heavier elements — hotter than red giants of the same mass; He burning releases more energy; chemical composition strongly affects the horizontal branch's morphology.
- Other regions: supergiants, brown dwarfs, white dwarfs.

> [!warning] IMPORTANT — why do massive stars evolve faster, if they have more H to burn?
> High-mass stars are much **hotter**, and so consume their H at a much **higher rate** — the extra fuel doesn't compensate for the disproportionately higher consumption rate.

> [!tip] While on the MS, a star barely moves on the HR diagram
> From the moment core H fusion begins, a star stays roughly in the same Main Sequence position for that entire phase. Only after exhausting central H does it evolve toward the giant branch.

## ⚡ Mass-luminosity relation

From the empirical relation between stellar mass and luminosity [Reid 1987]: $\uparrow$ mass $\Rightarrow$ $\uparrow$ temperature and $\uparrow$ luminosity. On a log-log scale, this relation is well described by a power law:

$$L \propto M^{\,\alpha}, \qquad \alpha \approx 4$$

valid over a limited mass range ($\sim0.1$ to $\sim10\,M_\odot$). This relation implies that spectral classification isn't just a temperature sequence, but also **a mass sequence** along the Main Sequence.

## ⏳ Main Sequence lifetime

Combining the Stefan-Boltzmann Law ($L = 4\pi R^2 \sigma T^4$) with the mass-energy equivalence of nuclear fusion ($E = mc^2$, considering that only $\sim$10% of a star's total mass is actually consumed in the core), the lifetime $t_{MS}$ is proportional to the ratio between available fuel mass and the consumption rate (luminosity):

$$t_{MS} \propto \frac{M}{L}$$

Combining this with the mass-luminosity relation ($L\propto M^4$):

$$t_{MS} \propto \frac{M}{M^4} = M^{-3}$$

i.e., **Main Sequence lifetime drops sharply with mass** — a star 10× more massive than the Sun lives, roughly, $10^3$ times shorter. This result is the quantitative basis for why massive stars evolve "too fast" despite their larger fuel reservoir, and connects directly with the role of cluster **turnoffs** as age clocks (Lecture 02).

> [!info]- A small complication
> HR diagrams built from real data (Hipparcos, Gaia) only contain stars with **estimated distances**. That's not always available — in those cases, one uses the **color-magnitude diagram** (the observational equivalent of the HR diagram, using apparent instead of absolute magnitude), the topic that opens Lecture 07.

---

## 📌 Key concepts

- **HR diagram:** temperature/color vs. luminosity/absolute magnitude; simultaneously reveals a star's mass, radius, and evolutionary stage.
- **Mass-luminosity relation:** $L \propto M^4$ (approx., for $0.1$–$10\,M_\odot$) — spectral classification is also a mass sequence.
- **MS lifetime $\propto M^{-3}$:** why massive stars, despite having more fuel, evolve much faster.

## 🔗 References and related

- Russell (1914) — original HR diagram
- Reid (1987) — mass-luminosity relation
- [CursoON — overview](en/resource/curso-on)
- [Lecture 02 — HR Diagram & Star Clusters](en/resource/curso-on/aula-02-diagrama-hr-e-aglomerados) — isochrones and turnoffs as age clocks
- [Lecture 07 — Distances, Distance Scale & Coordinates](en/resource/curso-on/aula-07-distancias-e-coordenadas)
