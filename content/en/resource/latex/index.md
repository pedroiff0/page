---
{"publish":true,"title":"📄 LaTeX and Academic Writing","created":"2026-07-23T00:08:52.669-03:00","modified":"2026-07-23T00:08:52.669-03:00","tags":["resources","latex","writing"]}
---

> [!note] Summary
> My own LaTeX course (5 lessons), from zero to writing your own classes, plus recommended materials and the essentials of ABNT formatting.

<div class="media-carousel">
  <a href="/en/resource/latex/lesson-01-setup" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="Lesson 01 — Setup & Environment" />
    <div class="slide-caption">Lesson 01 — Setup</div>
  </a>
  <a href="/en/resource/latex/lesson-02-basics" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="Lesson 02 — Basics" />
    <div class="slide-caption">Lesson 02 — Basics</div>
  </a>
  <a href="/en/resource/latex/lesson-03-templates" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="Lesson 03 — Templates & Classes" />
    <div class="slide-caption">Lesson 03 — Templates</div>
  </a>
  <a href="/en/resource/latex/lesson-04-intermediate" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="Lesson 04 — Intermediate" />
    <div class="slide-caption">Lesson 04 — Intermediate</div>
  </a>
  <a href="/en/resource/latex/lesson-05-advanced" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="Lesson 05 — Advanced" />
    <div class="slide-caption">Lesson 05 — Advanced</div>
  </a>
  <a href="/en/resource/latex/document-models" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="Document Models" />
    <div class="slide-caption">Document Models</div>
  </a>
</div>

## Why LaTeX?

Visual editors work fine until the day you need to number 40 equations, keep cross-references consistent, and format the bibliography in a journal's exact style — then they turn into enemies. LaTeX separates content from formatting: you write plain text with markup, and the system handles numbering, table of contents, citations and professional-quality typographic layout. Every paper I submit (including the work described in [Detecção de Anomalias em Dados do Gaia](pt-br/research/anomaly-detection)) is written in LaTeX.

## Course — 5 lessons

1. [Setup & Environment](en/resource/latex/lesson-01-setup) — TeX Live/MacTeX, VS Code + LaTeX Workshop, Overleaf, using AI carefully.
2. [Basics](en/resource/latex/lesson-02-basics) — minimal structure, lists, figures, tables, equations, document classes, essential packages.
3. [Templates & Classes](en/resource/latex/lesson-03-templates) — class vs. template, where to find them, how to adapt a ready-made one.
4. [Intermediate](en/resource/latex/lesson-04-intermediate) — project modularization, `\input` vs `\include`, centralized metadata.
5. [Advanced](en/resource/latex/lesson-05-advanced) — writing your own `.sty`/`.cls`, `@makeatletter`, custom environments.

After the 5 lessons: [Document Models](en/resource/latex/document-models) — a practical checklist per type (Thesis/ABNT, Report, Book, Beamer, Scientific poster).

## 📚 Recommended materials

- **[LaTeX handbook — basics to advanced](assets/biblioteca/latex-escrita/apostila-latex-ufes.pdf)** — PET Mecânica/UFES, free distribution (Portuguese).
- **[Figures and Diagrams with TikZ](assets/biblioteca/latex-escrita/figuras-diagramas-tikz-ufpb.pdf)** — Prof. Lenimar Andrade/UFPB (Portuguese).
- **[BibLaTeX Cheat Sheet](assets/biblioteca/latex-escrita/biblatex-cheatsheet.pdf)** and **[biblatex-abnt manual](assets/biblioteca/latex-escrita/biblatex-abnt-manual.pdf)** — free documentation ([CTAN](https://ctan.org/pkg/biblatex-abnt)).

## 🔗 References and related

- [Overleaf Learn](https://www.overleaf.com/learn) — the best introductory LaTeX documentation out there, with runnable examples. Start here.
- [abnTeX2](https://www.abntex.net.br) — the LaTeX class implementing Brazil's ABNT standards for theses and papers. The de facto standard for Brazilian undergraduate theses.
- [CTAN](https://ctan.org) — the official LaTeX package repository; every package's documentation lives here.
- [Detexify](https://detexify.kirelabs.org/classify.html) — draw the symbol you want and it tells you the LaTeX command.
- [Tables Generator](https://www.tablesgenerator.com) — generates LaTeX table code visually.
