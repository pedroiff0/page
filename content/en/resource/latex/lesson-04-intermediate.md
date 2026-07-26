---
publish: false
title: "Lesson 04 — Intermediate"
created: 2026-03-16
---

> [!note] Summary
> Why and how to modularize a LaTeX project: folder structure, `\input` vs `\include`, and centralizing metadata.

**Prerequisite**: [Lessons 01–03](en/resource/latex) (setup, basics, templates).

## Why modularize?

Easier to maintain long documents, reuse content/styles across projects, and isolate errors by compiling specific parts.

## Recommended project structure

```
project/
├── build/          # output (PDF, logs, aux files)
├── bib/            # bibliography (.bib)
├── img/            # figures and images
├── tex/            # chapters and preamble
│   ├── metadata.tex
│   ├── preamble.tex
│   ├── chap1.tex
│   └── chap2.tex
├── main.tex        # main file
└── Makefile        # (optional) build scripts
```

## `\input` vs `\include`

- `\input{file}` inserts the content as if it were in the same file.
- `\include{file}` creates auxiliary files (`.aux`) and is great for chapters.

```latex
% main.tex
\documentclass{report}
\begin{document}
\include{tex/chap1}
\include{tex/chap2}
\end{document}
```

## Metadata (centralize your work's info)

```latex
% tex/metadata.tex
\def\thetitle{Work Title}
\def\theauthor{Full Name}
\def\advisor{Prof. Dr. So-and-so}
\def\theyear{2026}
```

```latex
% main.tex
\input{tex/metadata}
\title{\thetitle}
\author{\theauthor}
\date{\theyear}
```

## 🔗 References and related

- [Course overview](en/resource/latex)
- [Lesson 03 — Templates & Classes](en/resource/latex/lesson-03-templates)
- [Lesson 05 — Advanced](en/resource/latex/lesson-05-advanced)
