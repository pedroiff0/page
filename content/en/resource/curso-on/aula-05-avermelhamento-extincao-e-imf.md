---
publish: false
password: "409182ph"
title: "Lecture 05 — Reddening, Extinction & IMF"
titulo: CursoON-Aula05
disciplina: Galactic Archaeology and Stellar Populations (National Observatory)
conteudo: The interstellar medium, extinction and reddening of starlight by dust, and the initial mass function revisited
professor: Hélio Dotto Perottoni
created: 2026-07-23
tags:
  - curso-on
  - galactic-archaeology
  - stellar-populations
  - interstellar-medium
  - interstellar-extinction
cssclasses:
  - page-grid
  - center-images
---
# 🌫️ Lecture 05 — Reddening, Extinction & IMF

> [!note] Summary
> Before any distance estimate in the Galaxy can be trusted, starlight must be corrected for the interstellar medium: gas and dust absorb and scatter photons in a wavelength-dependent way, attenuating (extinction) and reddening the observed light.

> [!info] Lecture info
> **Course:** Galactic Archaeology and Stellar Populations
> **Institution:** National Observatory (ON), Brazil
> **Professor:** Hélio Dotto Perottoni

---

## ☁️ The interstellar medium (ISM)

Gas and dust fill the space between stars: **~99%** of the ISM's mass is gas (neutral HI, ionized HII, molecular H₂), and **~1%** is dust. Of the gas mass, about 70% is hydrogen, 29% helium, and 1% metals. The ISM's distribution is **not homogeneous** across the galactic disk.

The total gas + dust mass represents only 10–20% of the Milky Way's stellar mass. Order-of-magnitude estimates for the Milky Way: total mass $1$–$1.5\times10^{12}\,M_\odot$; stellar mass $\sim5\times10^{10}\,M_\odot$; gas mass $\sim1\times10^{10}\,M_\odot$ — the rest is dark matter, whose distribution isn't directly observable (see [Understanding Dark Matter through Extragalactic Shocks](en/research/dark-matter-shocks) for an alternative, dynamical method of mapping it).

### Interstellar dust

Grains with an iron/silicate/graphite core, wrapped in frozen materials (CO₂/H₂O/NH₂) [Jessberger et al. 2001]. Scale comparison: atoms $\sim0.1\,$nm, small molecules $\sim1\,$nm, dust grains $\sim100\,$nm. Its distribution is quite **filamentary** — substantial variations occur across regions separated by just a few arcminutes [Argonaut 3D map].

### Forms of interstellar gas

- **HII (ionized hydrogen regions):** visible only near hot stars, whose UV light ionizes the gas — a small fraction of the total gas.
- **Neutral hydrogen clouds (HI):** don't emit in the visible; observed by absorption of starlight passing through them, or by the **21 cm** radio emission of cold H.
- **Ultra-hot gas:** temperatures of millions of degrees, from supernova explosions.
- **Molecular clouds:** complex molecules can survive when shielded from UV light; stellar nurseries.

Dust doesn't emit in the visible, but it **blocks** light — reflection nebulae are regions where dust scatters starlight, becoming visible mainly at blue wavelengths.

## 📉 The observational discovery of the interstellar medium

**Hartmann (1904)** observed the binary system **δ Orionis** and noticed that, while most spectral lines shifted consistently with the expected orbital motion (radial velocity variation for a binary), the Calcium K line **did not** share that variation. The correct conclusion: a stationary gas cloud containing calcium lay along the line of sight, between us and the binary system — the first direct evidence of diffuse matter in interstellar space.

## 🌒 Interstellar extinction

**Trumpler (1930)** found evidence for interstellar absorption by comparing open-cluster distances calculated two independent ways: stellar brightness vs. angular cluster diameter — the systematic discrepancy revealed that light was being attenuated by dust along the path. Trumpler showed that extinction roughly follows a $\lambda^{-1}$ law: if grains were much larger than $\lambda$, extinction would go as $\lambda^0$; if they were molecule-sized, it would be Rayleigh scattering ($\propto\lambda^{-4}$). The observed $\lambda^{-1}$ law implies grains of **intermediate** size.

### Definitions

- **Extinction ($A_\lambda$):** total light attenuation (absorption + scattering) at a given wavelength, measured in magnitudes. $A_V > 0$ always increases the observed apparent magnitude.
- **Reddening (color excess):** $E(B-V) = A_B - A_V$ — quantifies the color change caused by greater attenuation of short wavelengths relative to long ones.
- **Total-to-selective extinction ratio:** $A_V = R_V \cdot E(B-V)$, with $R_V \approx 3.1$ typical for the diffuse interstellar medium (ranges 2.7–6 in dense-cloud cores, an "anomalous" regime [Cardelli, Clayton & Mathis 1989]).

> [!warning] If you don't correct for extinction...
> ...you'll **systematically underestimate distances**, because stars dimmed by dust appear more distant than they actually are (via the distance modulus, Lecture 03).

Extinction mainly affects low galactic latitudes (where dust concentrates), but isn't zero off the plane — it must be accounted for whenever precise distances are needed.

### Cluster method for determining $R_V$

For a cluster, the intrinsic distance modulus $(m_V - M_V)_0$ is constant across all member stars. Observed variations in $(m_V - M_V)$ come from different amounts of extinction along each line of sight:

$$m_V - M_V = C + A_V = C + R_V\, E(B-V)$$

where $C$ is constant for the cluster (depends only on distance) and $A_V$ varies star by star.

### Extinction maps

The **Schlegel et al. (1998)** maps were built from far-infrared (FIR) data from the COBE mission, providing $E(B-V)$ for every sky direction. Modern tools: the `dustmaps` Python package, the Argonaut 3D map, and the IRSA/Caltech coordinate-lookup interface.

Basic practical correction: $\text{mag}_{x,0} = \text{mag}_x - \text{extinction coef.}_x \cdot E(B-V)_{\text{SFD}}$ (or multiplied by the Schlafly correction factor, $\times0.86$).

## 🧮 IMF — revisited

The **initial mass function** (see Lecture 02) describes the probability of star formation at each mass. It remains an active research object: uncertain in the very-high-mass limit ($\sim100\,M_\odot$), in the exact value of its characteristic peak, and regarding universality across different star-forming environments [Offner et al. 2014]. The IMF's exact shape is crucial for predicting timescales of chemical enrichment, supernova occurrence, and interstellar medium dynamics in a galaxy — directly connecting this lecture to the course's central theme.

---

## 📌 Key concepts

- **Extinction ($A_\lambda$) vs. reddening ($E(B-V)$):** total attenuation vs. differential color change — both caused by interstellar dust.
- **$R_V = A_V / E(B-V) \approx 3.1$:** characteristic ratio of the diffuse interstellar medium; used to convert color excess into total extinction.
- **Correcting for extinction is mandatory** for any reliable distance estimate — otherwise, distances are systematically overestimated.

## 🔗 References and related

- Trumpler (1930) — first evidence for interstellar extinction via clusters
- Cardelli, Clayton & Mathis (1989) — universal extinction law parametrized by $R_V$
- Schlegel, Finkbeiner & Davis (1998) — reference extinction maps
- Offner et al. (2014) — IMF review
- [CursoON — overview](en/resource/curso-on)
- [Lecture 02 — HR Diagram & Star Clusters](en/resource/curso-on/aula-02-diagrama-hr-e-aglomerados) — IMF first introduced
- [Lecture 06 — HR Diagram & Mass-Luminosity Relation](en/resource/curso-on/aula-06-diagrama-hr-e-relacao-massa-luminosidade)
- [Understanding Dark Matter through Extragalactic Shocks](en/research/dark-matter-shocks) — another (dynamical) method of mapping non-luminous mass, at extragalactic scale
