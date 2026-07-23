---
publish: true
title: "📐 Lecture 07 — Distances, Distance Scale & Coordinate Systems"
titulo: CursoON-Aula07
disciplina: Galactic Archaeology and Stellar Populations (National Observatory)
conteudo: The cosmic distance ladder — from radar to Type Ia supernovae — and the horizontal, equatorial, and galactic coordinate systems
professor: Hélio Dotto Perottoni
created: 2026-07-23
tags:
  - curso-on
  - galactic-archaeology
  - stellar-populations
  - distances
  - galactic-coordinates
cssclasses:
  - page-grid
  - center-images
---
# 📐 Lecture 07 — Distances, Distance Scale & Coordinate Systems

> [!note] Summary
> Distances establish the absolute scale for all of Astronomy. This lecture traces the "cosmic distance ladder" — from radar in the Solar System to Type Ia supernovae in distant galaxies — and closes with the three coordinate systems used to locate objects in the sky and in the Galaxy.

> [!info] Lecture info
> **Course:** Galactic Archaeology and Stellar Populations
> **Institution:** National Observatory (ON), Brazil
> **Professor:** Hélio Dotto Perottoni

---

## 🪜 The cosmic distance ladder

Each distance-measuring method is only valid within a range of scales, and the next method needs to be **calibrated** by the previous one — hence "ladder":

| Scale | Method | Typical range |
|---|---|---|
| Solar System | Radar | $10^{-4}$ light-years |
| Nearby stars | Trigonometric parallax | $10^3$ light-years |
| Milky Way | Main-sequence fitting (clusters) | $10^5$ light-years |
| Nearby galaxies | Cepheid variables (+ others) | $10^7$ light-years |
| Distant galaxies | Type Ia supernovae (standard candles) | $10^{10}$ light-years |

## 🛰️ Distances in the Solar System

**Kepler's 3rd Law** gives the **relative** distances between planets and the Sun — but an **absolute** measurement of at least one body is needed to calibrate the whole scale.

- **Giovanni Cassini (17th century):** first accurate estimate of the Astronomical Unit (AU $= 1.496\times10^{11}\,$m), via triangulating the distance to Mars, observed simultaneously from France and French Guiana. Off by only 7% from the current value.
- **Transit of Venus (mid-18th century):** an international campaign led by **Edmond Halley** (the same one from the comet) improves precision to 2%.
- **Radar (RAdio Detection And Ranging, early 1960s):** measures the time between emission and detection of a wave reflected off a solid surface; $d = c\,\Delta t / 2$. Values obtained already in the 1960s agree with current ones to the fifth decimal place. A key historical instrument was the **Arecibo radio telescope** (500 m), now decommissioned.

## ⭐ Trigonometric parallax

**Parallax** is the apparent shift in an object's position due to the observer's own motion — the same principle behind human depth perception (our two eyes as a baseline). By triangulation: $d = x/\tan\alpha$, where $x$ is the baseline and $\alpha$ the measured angle.

Our eyes only perceive depth at short range because the baseline (interpupillary distance) is tiny — for distant objects, $\alpha$ becomes imperceptible. In Astronomy, we have access to much larger baselines: **Earth's diameter**, or better still, **Earth's orbital diameter** (2 AU), observing the same object 6 months apart.

For small angles, $\tan p \approx p$, and defining $p$ in arcseconds leads to the **parsec** unit ("*parallax second*"): the distance of an object whose parallax is exactly 1 arcsecond:

$$d\,[\text{pc}] = \frac{1}{p\,['']}$$

**Friedrich Bessel (1838)** was the first to successfully measure a stellar parallax, for the star **61 Cygni** ($p=0.314'' \Rightarrow d=3.18\,$pc).

### The evolution of parallax measurements

- **Pre-Hipparcos:** ~1,000 stars with precise parallaxes (relative uncertainty <10%).
- **Hipparcos (1990s):** ~50,000 stars out to ~1 kpc.
- **Gaia (ongoing mission):** ~500 million stars out to ~10 kpc from the Sun — in units of milliarcseconds, corresponding to kiloparsec distances.

> [!tip] Looking up Gaia data
> To find data for a specific star in the Gaia catalog: look it up by name/coordinates in **SIMBAD** (`simbad.u-strasbg.fr`) — getting position, proper motion, radial velocity, parallax, and magnitudes across several bands — then cross-match the Gaia identifier with the full catalog via **VizieR** (`vizier.u-strasbg.fr`).

### Worked example — HD 249117

Measured parallax: $p = 0.3564 \pm 0.1343\,$mas (high uncertainty, since the star is too bright, $V<9$, for ideal Gaia measurements). Apparent magnitude $m=7.76$; calculated distance $\approx2.81\,$kpc. To correctly place the star on the HR diagram, it's still necessary to correct for extinction/reddening (Lecture 05) before converting to absolute magnitude.

## 🌌 Distances at the galactic scale — main-sequence fitting

Star clusters are groups of stars born approximately together — this is reflected in the distribution of their member stars on the HR diagram. Since apparent brightness depends on distance, and **all** stars in a given cluster are at the same distance, it's possible to fit a single theoretical model (isochrone) to all of them simultaneously, with **four free parameters**: age, chemical composition, reddening, and distance modulus [e.g., Oliveira et al. 2020, for the globular cluster Messier 69]. This would be impossible for a single isolated star, but with a cluster's thousands of stars constraining the fit simultaneously, it becomes tractable.

## 🌠 Distances to nearby galaxies — Cepheid variables

**Henrietta Leavitt** (early 20th century), studying variable stars in the Magellanic Clouds, noticed a relation between **pulsation period** and **brightness** for these stars — the **period-luminosity relation** ("Leavitt's Law") [1912HarCi.173....1L]. Cepheids are highly luminous pulsating stars, bright enough to be observed in nearby galaxies.

> [!warning] Calibration required
> To apply this relation as a distance measurement, one first needs to know the distance of **some** Cepheids by another method (parallax, clusters) — only then can the period-luminosity relation be calibrated on an absolute scale. Once calibrated, a Cepheid becomes a **standard candle**: its luminosity is known from the observed period, allowing distance to be computed directly.

**Edwin Hubble (1926)** used Cepheids to discover variables in Andromeda (M31), confirming it was in fact **another galaxy** rather than a nebula within the Milky Way — the milestone that established the existence of other galaxies exactly 100 years ago. In **1929**, Hubble used Cepheids in several nearby galaxies to show that (except for the closest ones, like M31 and the Magellanic Clouds) galaxies follow a linear relation between radial velocity and distance — **Hubble's Law**, whose slope is the Hubble constant, measuring the Universe's expansion rate.

## 💥 Distances to distant galaxies — Type Ia supernovae

Stars with mass close to the Sun's end their lives as **white dwarfs** (after the asymptotic giant branch phase and planetary nebula ejection). A key property of white dwarfs is the **Chandrasekhar mass limit** ($\sim1.4\,M_\odot$). In a binary system, a white dwarf can accrete material from a companion star; if it reaches the Chandrasekhar limit, a **Type Ia supernova** occurs.

Since all Type Ia SNe explode at nearly the same mass, they release very similar amounts of energy — their luminosities are well known and can be used as **standard candles** [K. Maguire 2017]. Unlike individual stars, supernovae can shine as bright as an entire galaxy, allowing distances to be measured accurately at scales far beyond any other method on the ladder.

### Full Hubble constant calibration chain

1. Cepheid parallaxes in the Milky Way;
2. Cepheids in nearby galaxies (e.g., M31);
3. Cepheids in galaxies that also hosted a Type Ia SN;
4. Type Ia SNe in distant galaxies.

Each rung depends on the previous one — hence "ladder."

## 🧭 Coordinate systems

### Horizontal

Fundamental planes: the horizon and the meridian (the vertical great circle including the zenith and celestial poles). Coordinates: **altitude** (angle between horizon and object), **zenith distance** (used to compute the airmass traversed by light in the atmosphere), and **azimuth** (angle between the meridian and the object's vertical, in the horizontal plane, East-West).

### Equatorial

Fundamental planes: the celestial equator and the hour circle (a great circle through the celestial poles and the object, perpendicular to the equator). Coordinates: **Right Ascension** ($\alpha$, measured from the vernal point, traditionally in h:m:s, but increasingly in degrees — e.g., the 2MASS catalog) and **Declination** ($\delta$, along the hour circle, from the equator to the object).

### Galactic

Fundamental planes: the galactic equator and meridians through the object and the galactic poles — the galactic plane is tilted **62°36'** relative to the celestial equator. Coordinates: **galactic longitude** ($l$, from the Sun–Galactic Center line, in the direction of galactic rotation) and **galactic latitude** ($b$, from the galactic plane to the object).

Quadrant convention: 1st ($0°<l<90°$), 2nd ($90°<l<180°$), 3rd ($180°<l<270°$), 4th ($270°<l<360°$). Before 1958, an older galactic coordinate system was used, counting longitude from one of the intersections between the galactic plane and celestial equator. Those coordinates are denoted $(l^I, b^I)$, in which the Galactic Center had coordinates $(327°41', -1°24')$; the current system is sometimes denoted $(l^{II}, b^{II})$ to distinguish it.

It's also common to represent an object's position in **Cartesian galactic coordinates** $(X,Y,Z)$, once the distance $d$ to the Sun is known — caution: different conventions use the X-axis pointing toward the Galactic Center or the Anticenter, or place the origin at the Galactic Center rather than the Sun.

### Precession of the equinoxes

Because Earth isn't a perfect sphere, differential torques from the Moon and Sun on its equator cause its rotation axis to **precess**, with a ~25,800-year period — shifting the vernal point's position and, therefore, every object's equatorial coordinates over time (~1 arcminute/year along the ecliptic). Astronomical coordinates are therefore only fully meaningful when given together with the **reference equinox** (standard epochs: 1875.0, 1950.0, 2000.0, 2025.0; the Hipparcos catalog's coordinates are valid for epoch 1991.5). Before observing, catalog coordinates must be precessed to the current date.

---

## 📌 Key concepts

- **Cosmic distance ladder:** each method (radar → parallax → MS fitting → Cepheids → Type Ia SNe) calibrates the next, spanning $10^{-4}$ to $10^{10}$ light-years.
- **Parsec:** distance corresponding to a parallax of 1 arcsecond; $d\,[\text{pc}] = 1/p['']$.
- **Standard candle:** an object of known intrinsic luminosity (Cepheids via the P-L relation; Type Ia SNe via the Chandrasekhar limit) — converts apparent brightness directly into distance.
- **Galactic coordinates $(l,b)$:** system with its fundamental plane in the Milky Way's disk, essential for any galactic archaeology study.

## 🔗 References and related

- Bessel (1838) — first successfully measured stellar parallax
- Leavitt (1912) — Cepheid period-luminosity relation
- Hubble (1926, 1929) — Cepheids in M31; Hubble's Law
- Oliveira et al. (2020) — isochrone fitting for Messier 69
- [CursoON — overview](en/resource/curso-on)
- [Lecture 03 — Magnitudes, Colors & Spectral Classification](en/resource/curso-on/aula-03-magnitudes-cores-e-classificacao-espectral) — distance modulus
- [Lecture 08 — Velocities & Proper Motion](en/resource/curso-on/aula-08-velocidades-e-movimento-proprio)
