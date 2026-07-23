---
{"publish":true,"title":"🧩 Lesson 03 — Templates & Classes","created":"2026-03-16","modified":"2026-07-23T00:09:26.061-03:00"}
---

> [!note] Summary
> The difference between a class and a template, where to find ready-made templates, and how to adapt one for a different use.

**Prerequisite**: [Lesson 02](en/resource/latex/lesson-02-basics) to understand `.tex` structure.

## 1. Key concepts

- **Class** (`.cls`): defines the document's core structure (heading types, margins, list behavior, etc.) — `article`, `report`, `book`, `abntex2`, `beamer`.
- **Template**: a set of files (`.tex`, `.sty`, `.cls`, `.bib`, images) pre-configured for a specific document type (thesis, paper, presentation).

## 2. Where to find templates

- [Overleaf Templates](https://www.overleaf.com/latex/templates)
- [CTAN](https://ctan.org/) — Comprehensive TeX Archive Network

## 3. Using a template (step by step)

1. Download the template into your project.
2. Open it in VS Code (or Overleaf).
3. Identify the main files: `main.tex`, `*.cls`, `*.sty`, `bibliography.bib`.
4. Make a backup copy before editing.
5. Customize the front matter (cover, abstract, author info) and chapter structure.

## 4. Adapting a template for another use

- Replace chapter content while keeping the file structure.
- Update the `\include`/`\input` lines for your chapters.
- Adjust any config file (name, advisor, etc.).
- Compile after every change to isolate errors.

## 5. Useful model examples

- Thesis/report (ABNT-style): `abntex2`.
- Scientific paper: `article` with `IEEEtran`, `Elsevier`, `elsarticle`.
- Presentation: `beamer` or `powerdot`.
- Academic poster: `sciposter`, `a0poster`, `tikzposter`.

See [Document Models](en/resource/latex/document-models) for ready-to-use examples of each.

## 🔗 References and related

- [Course overview](en/resource/latex)
- [Lesson 02 — Basics](en/resource/latex/lesson-02-basics)
- [Lesson 04 — Intermediate](en/resource/latex/lesson-04-intermediate)
- [Document Models](en/resource/latex/document-models)
