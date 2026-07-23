---
{"publish":true,"title":"✨ Lecture 03 — Magnitudes, Colors & Spectral Classification","created":"2026-07-23","modified":"2026-07-23T00:25:25.152-03:00","tags":["curso-on","galactic-archaeology","stellar-populations","photometry"],"cssclasses":["page-grid","center-images"]}
---

# ✨ Lecture 03 — Magnitudes, Colors & Spectral Classification

> [!note] Summary
> How to quantify stellar brightness — from Hipparchus's scale to absolute magnitude — and how color indices derived from that scale let us infer temperature for thousands of stars without needing an individual spectrum for each one.

> [!info] Lecture info
> **Course:** Galactic Archaeology and Stellar Populations
> **Institution:** National Observatory (ON), Brazil
> **Professor:** Hélio Dotto Perottoni

---

## 💡 Light propagation and the brightness–distance degeneracy

Luminous flux (energy emitted per unit area) decreases with the square of the distance to the source (inverse-square law). This creates a **degeneracy** between intrinsic brightness (luminosity) and distance: observing a bright object in the sky, apparent brightness alone can't tell us whether it's intrinsically luminous and far away, or faint and nearby. That's why what we always observe directly is **apparent brightness** — measured in practice by counting the number of photons received (today, via CCD).

## 📏 The magnitude scale

**Hipparchus** (190–120 BC) established the first comparative scale of stellar brightness, from 1 (brightest) to 6 (limit of human vision). Between magnitudes 1 and 6 there's a 100× difference in flux — so each magnitude step corresponds to a factor of $100^{1/5} \approx 2.512$ in flux. The formal definition:

$m_1 - m_2 = -2.5 \log_{10}\left(\frac{F_1}{F_2}\right)$

The negative sign imposes the **inverse** relation between magnitude and brightness: the **smaller** the magnitude, the **brighter** the object.

### Absolute magnitude

**Absolute magnitude ($M$)** is the magnitude a star would have if placed exactly **10 parsecs** from the Sun — a measure of intrinsic brightness, free from the distance degeneracy. The difference between apparent and absolute magnitude is the **distance modulus**:

$m - M = 5\log_{10}(d) - 5 \quad (d \text{ in parsecs})$

This is one of the fundamental equations of Astronomy. Example: knowing that the distance modulus of the Large Magellanic Cloud (LMC) is 18.5, and that the Sun's absolute magnitude is $\approx4.8$, a solar-type star in the LMC would have apparent magnitude $m = 18.5 + 4.8 = 23.3$.

## 🎨 Magnitude and photometric systems

- **VEGA magnitudes:** based on the star Vega, defined with $V\approx0.03$ and colors $\approx0$ by construction. The zero-point depends on Vega's spectrum in each band.
- **AB magnitudes:** defined by a constant absolute physical flux (independent of any reference spectrum).
- **griz / Gunn / Oke:** based on observational calibration, historically tied to standard stars (e.g., F subdwarfs).

> [!warning] A magnitude system is not a filter system
> You can use any filter within any magnitude system — the two are independent concepts. Several photometric systems have been developed for different applications and wavelength ranges \[Almeida-Fernandes et al. 2021; Perottoni et al. 2024].

## 🌈 Color indices

In Astronomy, a **color** (or color index) is the difference between an object's magnitude in two spectral bands — e.g., $B-V$ (Johnson/UBV system). In the absence of selective absorption, colors are **independent of distance** (the brightness degeneracy cancels out in the subtraction). Vega has all colors equal to 0 in the VEGAmag system, by construction.

Considering blackbody spectra for three stars with $T_a > T_b > T_c$:

- $T_a = 30{,}000\,$K: flux in B greater than in V → $B-V < 0$ (bluer)
- $T_b = 10{,}000\,$K: flux in B $\approx$ flux in V → $B-V \sim 0$
- $T_c = 3{,}000\,$K: flux in B smaller than in V → $B-V > 0$ (redder)

Color indices are extremely useful in practice: they let you estimate a physical property (temperature) for thousands of stars at once, without the cost of obtaining an individual spectrum for each.

## 🔬 Spectral classification

### Historical development

- **Late 19th century (~1890):** Harvard University obtains spectra for ~10,000 stars; **Williamina Fleming** develops the foundations of modern classification based on hydrogen line intensity; the **Henry Draper Catalog (HD)** is born.
- **Early 20th century (~1910):** with a sample of ~200,000 spectra, **Annie Jump Cannon** refines the classification by considering the correlation between spectral type and color (i.e., temperature) — the **Harvard Classification** is born.

### The OBAFGKM sequence

Cannon's classification uses 7 main classes, organized by **decreasing temperature** (not alphabetical order, since it's an adaptation of Fleming's original scheme):

| Type | Temperature | Dominant lines |
|---|---|---|
| O | Hottest | He II (ionized) |
| B | Very hot | C, He I (neutral) |
| A | Hot | H (strongest in the entire sequence) |
| F–G | Intermediate | Metals in general (Sun is G) |
| K–M | Cool | Metal lines / molecules (TiO in M) |

The peak of the class M spectrum is shifted to longer wavelengths, while type O emits most intensely at small $\lambda$ — **Wien's Law** in action. Type A stars ($\sim$10,000 K) have the most intense hydrogen absorption lines of the entire sequence (see Lecture 04 for the physical explanation, via the population of hydrogen's energy levels).

## 📷 Types of photometry

- **Absolute photometry:** measures brightness on a calibrated, physical scale, allowing comparison of objects across different sky regions (_all sky_). Requires a photometric night and calibration with standard stars — more sensitive to atmospheric variation.
- **Differential photometry:** measures brightness relative to other stars in the same field, observed simultaneously in the same image. Less affected by atmospheric conditions; works even without a perfectly photometric night.
- **Time-domain photometry:** tracks brightness variations of the same object over time (essential for identifying variables, such as the Cepheids of Lecture 07).

---

## 📌 Key concepts

- **Apparent vs. absolute magnitude:** the latter removes the distance degeneracy — their difference is the distance modulus, $m - M = 5\log_{10}d - 5$.
- **Color index:** difference of magnitudes in two bands; a cheap, distance-independent proxy for effective temperature.
- **OBAFGKM:** decreasing temperature sequence; type A has the strongest H lines.

## 🔗 References and related

- Almeida-Fernandes et al. (2021) — photometric systems
- Perottoni et al. (2024) — photometric calibration (GaiaXPy)
- [CursoON — overview](en/resource/curso-on)
- [Lecture 02 — HR Diagram & Star Clusters](en/resource/curso-on/aula-02-diagrama-hr-e-aglomerados)
- [Lecture 04 — Spectroscopy & Metallicity](en/resource/curso-on/aula-04-espectroscopia-e-metalicidade)
- [Winter School — Galactic Archaeology, Lecture 01](pt-br/resource/escolainverno/arqgal/arqueologiagalactica-aula01) — OBAFGKM classification revisited in a nucleosynthesis context (Portuguese only)
