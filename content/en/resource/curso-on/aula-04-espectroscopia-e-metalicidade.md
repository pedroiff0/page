---
publish: true
title: "Lecture 04 — Spectroscopy & Metallicity"
titulo: CursoON-Aula04
disciplina: Galactic Archaeology and Stellar Populations (National Observatory)
conteudo: Kirchhoff's laws, spectral line formation, the discovery of helium, and the [Fe/H] metallicity notation
professor: Hélio Dotto Perottoni
created: 2026-07-23
tags:
  - curso-on
  - galactic-archaeology
  - stellar-populations
  - spectroscopy
  - metallicity
cssclasses:
  - page-grid
  - center-images
---
# 🔭 Lecture 04 — Spectroscopy & Metallicity

> [!note] Summary
> Spectroscopy is the indispensable foundation of modern astrophysics: it reveals chemical composition, motion, and distance from how matter emits and absorbs radiation. This lecture traces the physics of spectral line formation and arrives at the [Fe/H] notation used across all of galactic archaeology to measure metallicity.

> [!info] Lecture info
> **Course:** Galactic Archaeology and Stellar Populations
> **Institution:** National Observatory (ON), Brazil
> **Professor:** Hélio Dotto Perottoni

---

## 🌈 Modern spectroscopy

Spectroscopy links the properties observed in spectra (spectral lines and their intensities) to physical phenomena occurring in extraterrestrial environments — electronic transitions of different energies in stars, nebulae, planets, etc. This is the technique that let **Cecilia Payne** discover/interpret the Sun's chemical composition (see below). The basic apparatus of a spectrograph is: source → slit → prism (today, a diffraction grating) → CCD.

## 🔎 The discovery of helium

A sequence of milestones in the early 19th/20th centuries:

- **William Wollaston (1802):** discovers dark lines in the Sun's spectrum.
- **Joseph Fraunhofer (1814):** catalogs ~570 dark lines — the "Fraunhofer spectrum," a term still used today.
- **Henry Draper (1872):** pioneer of stellar spectroscopy.
- **Jules Janssen (1868):** observes an unidentified dark line in the solar spectrum.
- **Norman Lockyer (1868):** identifies that same line and proposes it's due to a previously unknown element — **helium**, named before it was ever isolated in a laboratory on Earth.

## ⚖️ Kirchhoff's laws

1. Solids, liquids, or very dense gases, when heated, produce **continuous spectra**.
2. Low-density gases, when heated, produce **emission spectra**.
3. Low-density gases in front of a continuous-spectrum source produce **absorption spectra** — provided the gas is cooler than the source.

Every chemical element has a unique, characteristic set of lines — this is what allows an element to be identified through its spectrum.

## ⚛️ Spectral line formation

An electron bound to a nucleus has a **ground state** (minimum energy) and an **ionization energy** (above which it's no longer bound — the atom becomes an ion). Between these two limits, the electron can only occupy **discrete energy levels**. The energy of the photon emitted/absorbed in a transition is:

$$\Delta E = h\nu = \frac{hc}{\lambda} = E_0\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)$$

where $E_0 = -13.6\,$eV is hydrogen's ionization potential (Rydberg's formula).

The development of the Harvard Classification (~1910–1920) coincides with **Bohr's atomic model**, which explains why hydrogen line intensity varies with stellar temperature:

- **Low temperatures:** the H atom typically stays in the ground state → **weaker** H lines (lower transition frequency).
- **Intermediate temperatures:** higher probability of the electron occupying the first excited state (level 2) → **Balmer series** transitions occur, detectable in the visible. This is why **A-type stars** have the **strongest** H lines of the entire spectral sequence.
- **High temperatures:** above $\sim$10,000 K, hydrogen ionizes rapidly → less neutral H → weaker lines again. That's why O- and B-type stars have weaker H lines than A-type stars.

## 🧪 Stellar composition: Cecilia Payne

Understanding atomic excitation/ionization processes allowed the calculation of spectral line intensities as a function of temperature — work by **Cecilia Payne**, who demonstrated that the amounts of **H and He are far greater** than any other element in stars (and, by extension, in the Universe). In the early 20th century, data quality still didn't allow distinguishing fine differences in chemical composition between stars; today, high-resolution spectra (more pixels per wavelength) allow detailed determinations — fundamental for understanding stellar evolution and the production of the periodic table's elements.

Comparing spectra of stars with similar spectral type, an increase in the number/intensity of lines indicates a **decrease** in the amount of elements heavier than H and He — the **metals**, in the astronomical sense: literally any element besides hydrogen and helium. It's generally assumed the observed surface composition reflects the original composition of the gas cloud the star formed from.

## 🔢 Metallicities and abundances

Early stellar evolution models considered only three abundance components: hydrogen ($X$), helium ($Y$), and metals ($Z$), with $X+Y+Z=1$. Spectroscopically, one assumes $Z \propto n(\text{Fe})$, giving rise to the standard notation:

$$[\text{Fe/H}] = \log_{10}\left(\frac{N_{Fe}/N_H}{(N_{Fe}/N_H)_\odot}\right)$$

Equivalently, an abundance ratio between any two elements, $[X/Y]$, can be defined.

### Interpreting [Fe/H]

| Value | Interpretation |
|---|---|
| $[\text{Fe/H}] > 0$ | metal-rich — more metal-rich than the Sun |
| $[\text{Fe/H}] < 0$ | metal-poor — more metal-poor than the Sun |
| $[\text{Fe/H}] = -1$ | 10× less iron than the Sun |
| $[\text{Fe/H}] = -2$ | 100× less iron |
| $[\text{Fe/H}] = -3$ | 1000× less iron |
| $[\text{Fe/H}] = -4$ | 10000× less iron |

[Beers & Christlieb 2005] is the classic reference for searching and characterizing extremely metal-poor stars — the oldest fossils accessible to galactic archaeology.

### Photometric metallicity

Metallicity can also be estimated from **photometry** (colors) alone, without spectroscopy — a cheaper alternative for large surveys, though less precise [Babusiaux et al. 2018].

---

## 📌 Key concepts

- **Kirchhoff's laws:** continuous spectrum (dense hot source) vs. emission (hot rarefied gas) vs. absorption (cool rarefied gas in front of a continuous source).
- **Balmer series:** optical H transitions responsible for the peak in H line intensity in A-type stars.
- **[Fe/H]:** Sun-relative logarithmic notation; the quantitative basis of all of the Galaxy's chemical archaeology.

## 🔗 References and related

- Beers & Christlieb (2005) — metal-poor stars
- Babusiaux et al. (2018) — photometric metallicity with Gaia data
- [CursoON — overview](en/resource/curso-on)
- [Lecture 03 — Magnitudes, Colors & Spectral Classification](en/resource/curso-on/aula-03-magnitudes-cores-e-classificacao-espectral)
- [Lecture 05 — Reddening, Extinction & IMF](en/resource/curso-on/aula-05-avermelhamento-extincao-e-imf)
- [Winter School — Galactic Archaeology, Lecture 01](pt-br/resource/escolainverno/arqgal/arqueologiagalactica-aula01) — [Fe/H] and [α/Fe] notation applied to population separation (Portuguese only)
- [Anomaly Detection in Gaia Data](en/research/anomaly-detection) — my research uses GALAH DR4 spectra processed with the same principles seen here
