---
publish: false
title: "Lesson 02 — Basics"
created: 2026-03-16
---

> [!note] Summary
> Minimal document structure, lists, alignment, figures, tables, equations, document classes, and the essential packages.

**Prerequisite**: [Lesson 01](en/resource/latex/lesson-01-setup) (setup & environment).

## 1. Minimal document structure

```latex
\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lipsum} % sample text

\title{Document Title}
\author{Your Name}
\date{\today}

\begin{document}
\maketitle
\tableofcontents

\section{Introduction}
\lipsum[1]

\section{Body}
\subsection{Subsection}
\lipsum[2]

\end{document}
```

`\tableofcontents` auto-generates the index; use `\section`, `\subsection`, `\subsubsection` to organize.

## 2. Basic text formatting

```latex
\begin{itemize}
  \item Simple item
  \item Another item
\end{itemize}

\begin{enumerate}
  \item First
  \item Second
\end{enumerate}
```

```latex
\begin{flushleft}Left-aligned text.\end{flushleft}
\begin{center}Centered text.\end{center}
\begin{flushright}Right-aligned text.\end{flushright}
```

## 3. Figures and tables

```latex
\usepackage{graphicx}

\begin{figure}[ht]
  \centering
  \includegraphics[width=0.7\textwidth]{example.png}
  \caption{Figure caption.}
  \label{fig:example}
\end{figure}
```

```latex
\begin{table}[ht]
  \centering
  \begin{tabular}{|l|c|r|}
    \hline
    Name & Age & Score \\
    \hline
    Ana & 23 & 8.5 \\
    John & 25 & 9.1 \\
    \hline
  \end{tabular}
  \caption{Example table.}
  \label{tab:example}
\end{table}
```

## 4. Equations

```latex
\usepackage{amsmath}

\begin{equation}\label{eq:pythagoras}
  a^2 + b^2 = c^2
\end{equation}
```

For unnumbered equations, use `\[ ... \]` or `\begin{equation*}`.

## 5. Document classes (when to use which)

- `article`: papers, short reports.
- `report`: chapters, theses, larger works.
- `book`: books with chapters, frontmatter/backmatter.
- `beamer`: presentations.

## 6. Essential packages

- `graphicx`, `amsmath`, `hyperref`, `geometry`, `fontenc`/`inputenc`/`babel`.
- For thesis-style formatting: `abntex2`/`abntex2cite` (Brazil-specific), `tocloft`, `biblatex`/`natbib` + `biber`.

## 7. Preamble configuration

```latex
\documentclass[12pt,a4paper]{report}
\usepackage[top=3cm,bottom=3cm,left=3cm,right=3cm]{geometry}
\usepackage{setspace}
\doublespacing
\usepackage{fancyhdr}
\pagestyle{fancy}
```

Changing the font (XeLaTeX/LuaLaTeX):

```latex
\usepackage{fontspec}
\setmainfont{TeX Gyre Termes}
```

## 🔗 References and related

- [Course overview](en/resource/latex)
- [Lesson 01 — Setup](en/resource/latex/lesson-01-setup)
- [Lesson 03 — Templates & Classes](en/resource/latex/lesson-03-templates)
