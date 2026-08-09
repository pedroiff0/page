---
publish: false
title: "Articles"
created: 2026-07-23
modified: 2026-07-25T23:58:08.061-03:00
published: 2026-07-25T23:58:08.061-03:00
order: 1
---

> [!note] Summary
> Reading notes on 28 scientific articles relevant to the project [Gaia Data Anomalies Detection](/en/research/anomaly-detection), organized by theme.


<div class="media-carousel">
  <a href="/pt-br/research/anomaly-detection/articles/collaboration2016" class="carousel-slide">
    <img src="/assets/illustrations/articles.svg" alt="The Gaia Mission" />
    <div class="slide-caption">The Gaia Mission</div>
  </a>
  <a href="/pt-br/research/anomaly-detection/articles/buder2025" class="carousel-slide">
    <img src="/assets/illustrations/articles.svg" alt="GALAH DR4" />
    <div class="slide-caption">GALAH DR4</div>
  </a>
  <a href="/pt-br/research/anomaly-detection/articles/majewski2017" class="carousel-slide">
    <img src="/assets/illustrations/articles.svg" alt="APOGEE" />
    <div class="slide-caption">APOGEE</div>
  </a>
  <a href="/pt-br/research/anomaly-detection/articles/deandrade2025" class="carousel-slide">
    <img src="/assets/illustrations/articles.svg" alt="GCNS × GALAH DR4" />
    <div class="slide-caption">GCNS × GALAH DR4</div>
  </a>
  <a href="/pt-br/research/anomaly-detection/articles/traven2017" class="carousel-slide">
    <img src="/assets/illustrations/articles.svg" alt="GALAH — Classification via t-SNE" />
    <div class="slide-caption">GALAH — Classification via t-SNE</div>
  </a>
  <a href="/pt-br/research/anomaly-detection/articles/lochner2021" class="carousel-slide">
    <img src="/assets/illustrations/articles.svg" alt="ASTRONOMALY" />
    <div class="slide-caption">ASTRONOMALY</div>
  </a>
</div>


 Reading notes on scientific articles relevant to my research in detecting anomalies in stellar populations — own syntheses, not complete articles (editors/arXiv copyrights remain with the original authors). Grouped by role in the project: the surveys and data I use, the machine learning methods I apply, the stellar models that calibrate my ages/isochrons, and the context of galactic dynamics/chemistry that interprets the results.

## 🛰️ Surveys and catalogues (data)

- [The Gaia Mission](/en/research/anomaly-detection/articles/collaboration2016)— astrometry of billions of stars; source of the project's kinematic coordinates.
- [Gaia EDR3 — Gaia Catalog of Nearby Stars](/en/research/anomaly-detection/articles/collaboration2021)— clear catalogue at 100 ch of the Sun, basis of sample GCNS.
- [GCNS × GALAH DR4](/en/research/anomaly-detection/articles/deandrade2025)— my own article, the joint analysis under Step 1.
- [GALAH DR4](/en/research/anomaly-detection/articles/buder2025)— GALAH 4th release: up to 32 elements per star via neural networks.
- [GALAH — Data Reduction Pipeline](/en/research/anomaly-detection/articles/kos2017)— how the raw spectra of HERMES saw the parameters of the catalogue.
- [APOGEE](/en/research/anomaly-detection/articles/majewski2017)— high-resolution infrared survey, used as comparison/context.
- [LAMOST DR5 — Abundances of 16 Elements](/en/research/anomaly-detection/articles/xiang2019)— another large-volume spectroscopic survey, date-driving approach (DD-Payne).
- [S-PLUS DR4 — SED Outliers](/en/research/anomaly-detection/articles/quispehuaynasi2025)— detection of photometric anomalies in different survey, methodological parallel.

## 🤖 Machine learning and anomaly detection

- [GALAH — Classification via t-SNE](/en/research/anomaly-detection/articles/traven2017)— Stage 2 basic methodology (t-SNE on crude spectra).
- [da Silva & Smiljanic (2023) — t-SNE Chemodynamics](/en/research/anomaly-detection/articles/dasilva2023)— the basis of the comparison between catalogue columns and spectrum pixels.
- [ASTRONOMALY](/en/research/anomaly-detection/articles/lochner2021)— motivation of scale: why big astronomical data requires automatic detection of anomalies.
- [Active Detection of Anomalies (Time-Domain)](/en/research/anomaly-detection/articles/ishida2021)—  active learning  applied to the discovery of unusual objects.
- [Machine Learning for Binary](/en/research/anomaly-detection/articles/traven2019)— revision of LM methods in large surveys.
- [GALAH — Emission Line Stars](/en/research/anomaly-detection/articles/otar2021)— self-encoder that rebuilds spectra to find abnormal emissions — same family of Step 2 method.
- [GALAH — Extremely Poor Stars in Metals](/en/research/anomaly-detection/articles/hughes2022)— LM supervised to find 54 EMP candidates at GALAH.
- [GALAH — Diffuse Interstellar Bands](/en/research/anomaly-detection/articles/vogrini2023)— another example of GALAH  big data  spectroscopic mining.

## ⭐ Star models and ages

- [PARSEC — Star Isochrons](/en/research/anomaly-detection/articles/bressan2012)— stellar evolution code generating isochrons used in the Kiel diagram.
- [PARSEC-COLIBRI — TP-AGB Phase Isochrons](/en/research/anomaly-detection/articles/marigo2017)— the latest generation of isochrons, with a detailed TP-AGB phase.
- [GALAH — Chemical clocks](/en/research/anomaly-detection/articles/hayden2022)— age via XGBoost from metalicity only/abundances.
- [GALAH — FGK Binaries](/en/research/anomaly-detection/articles/traven2020)— sample of spectroscopic binaries, relevant for cleaning contaminants from the sample.
- [SpectroTranslator](/en/research/anomaly-detection/articles/thomas2024)— neural network to convert parameters between different surveys.

## 🌌 Dynamics and galactic chemistry (interpretation)

- [galpy](/en/research/anomaly-detection/articles/bovy2015)— package used to calculate orbits and actions, base of the project kinematics.
- [Milky Way Mass and Potential Distribution](/en/research/anomaly-detection/articles/mcmillan2017)— the galactic potential used in galpy to integrate orbits.
- [GALAH — Chemical Dynamics of Solar Neighborhood](/en/research/anomaly-detection/articles/hayden2020)— reference chemodynamic structure for comparison with cross-sample.
- [Gaia-ESO — Fine/Spense Disk Transition](/en/research/anomaly-detection/articles/recioblanco2014)— the context of star populations and radial migration.
- [Co-formation of Fine/Spense Discs (z>2)](/en/research/anomaly-detection/articles/borbolato2025)— training scenario for fine disc dichotomy/expenditure.
- [Star Life Times and Abundance Reasons](/en/research/anomaly-detection/articles/tinsley1979)— classical article of chemical evolution, theoretical basis of nucleosynthesis.
- [Abundances in Dwarfs G VI](/en/research/anomaly-detection/articles/wallerstein1962)— historical article, one of the first systematic determinations of stellar abundance.

> [!abstract] Automatic translation notice
> This page was automatically translated from Portuguese using the LibreTranslate-based automated translator implemented in `tools/translate_quartz.py` (it preserves wikilinks, embeds and proper names via positional splitting). Machine translation may contain inaccuracies — the original Portuguese version is the authoritative source.
