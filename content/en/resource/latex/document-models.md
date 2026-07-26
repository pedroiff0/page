---
publish: false
title: "Document Models"
created: 2026-03-17
---

> [!note] Summary
> Ready-to-use minimal structure for the most common document types: Report, Book, Beamer (slides), scientific poster, and the thesis checklist.

## Report (`report`)

```latex
\documentclass[12pt,a4paper]{report}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{hyperref}

\title{Report Title}
\author{Your Name}
\date{\today}

\begin{document}
\maketitle
\tableofcontents

\chapter{Introduction}
Introduction text.

\chapter{Methodology}
Methodology text.

\chapter{Results}
Results text.

\chapter{Conclusion}
Conclusion text.

\end{document}
```

## Book (`book`)

```latex
\documentclass[12pt,a4paper]{book}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}

\title{Book Title}
\author{Your Name}
\date{\today}

\begin{document}
\frontmatter
\maketitle
\tableofcontents

\mainmatter
\chapter{First Chapter}
Chapter text.

\backmatter
\chapter{References}
\end{document}
```

## Beamer (presentations)

```latex
\documentclass{beamer}
\usetheme{Madrid}
\usecolortheme{seahorse}

\title{Presentation Title}
\author{Your Name}
\date{\today}

\begin{document}

\begin{frame}
  \titlepage
\end{frame}

\begin{frame}{Agenda}
  \tableofcontents
\end{frame}

\end{document}
```

## Scientific poster (`sciposter`)

```latex
\documentclass[a0paper,portrait]{sciposter}
\usepackage[utf8]{inputenc}
\usepackage{graphicx}
\usepackage{xcolor}

\title{Poster Title}
\author{Your Name}
\institute{Institution}

\begin{document}
\maketitle

\begin{multicols}{2}
  \section{Introduction}
  Introduction text.

  \section{Methodology}
  Methodology text.

  \section{Results}
  Results text.

  \section{Conclusion}
  Conclusion text.
\end{multicols}

\end{document}
```

> [!tip] Quick tips
> Use high-resolution images (PNG/PDF). Control spacing with `\vspace`/`\hspace`, and `\columnsep` for column gaps. For more graphical control, try `tikzposter`.

## Thesis (ABNT checklist)

The thesis template (via `abntex2`) covers, among others: cover, title page, catalog card, approval page, acknowledgments, dedication, epigraph, errata, abstract, lists of figures/tables/symbols, table of contents, introduction/methodology/development/conclusion, references (ABNT), glossary, appendices, attachments and index — with dedicated environments for algorithms, boxes and charts, and automatic numbering of appendices/attachments.

Standard formatting: Arial 12, justified, 1.25 cm indent, uniform spacing on centered headings.

## 🔗 References and related

- [Course overview](en/resource/latex)
- [Lesson 03 — Templates & Classes](en/resource/latex/lesson-03-templates)
- [abnTeX2](https://www.abntex.net.br)
