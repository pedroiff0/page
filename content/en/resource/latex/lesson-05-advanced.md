---
{"publish":true,"title":"⚙️ Lesson 05 — Advanced","created":"2026-03-16","modified":"2026-07-23T00:09:44.593-03:00"}
---

> [!note] Summary
> Writing your own packages (`.sty`) and classes (`.cls`), `@makeatletter`, custom environments, and advanced compilation.

**Prerequisite**: [Lessons 01–04](en/resource/latex) (setup, basics, templates, modularization).

## 1. Writing packages (`.sty`)

A package lets you share styles and commands across documents.

```latex
% mystyle.sty
\ProvidesPackage{mystyle}[2026/03/17 v1.0]

\RequirePackage{geometry}
\RequirePackage{graphicx}

\newcommand{\mycommand}[1]{\textbf{#1}}

\endinput
```

## 2. Writing classes (`.cls`)

```latex
% myclass.cls
\ProvidesClass{myclass}[2026/03/17 v1.0]
\LoadClass{article}

\RequirePackage{geometry}
\RequirePackage{titlesec}

\titleformat{\section}{\Large\bfseries}{\thesection}{1em}{}
```

## 3. `@makeatletter` and internal commands

```latex
\makeatletter
\def\@my@thing{...}
\makeatother
```

## 4. Creating and redefining environments

```latex
\renewenvironment{quote}
  {\begin{center}\itshape}
  {\end{center}}
```

```latex
\newenvironment{mybox}[1]
  {\begin{center}\fbox{\begin{minipage}{0.9\linewidth}\textbf{#1}\\}}
  {\end{minipage}}\end{center}}
```

## 5. Special lists and custom indexes

`\listoffigures` / `\listoftables` / `\listof{lol}{Title}`, or custom lists with `enumitem`/`tocloft`.

## 6. Advanced compilation

`latexmk -pdf -pvc` for watch mode, `xelatex`/`lualatex` for better Unicode/system font support, `make`/`arara` for complex build pipelines.

## 🔗 References and related

- [Course overview](en/resource/latex)
- [Lesson 04 — Intermediate](en/resource/latex/lesson-04-intermediate)
- [LaTeX class guide](https://www.latex-project.org/help/documentation/clsguide.pdf)
