---
publish: false
title: "Lesson 01 — Setup & Environment"
created: 2026-03-16
---

> [!note] Summary
> Installing TeX Live/MacTeX, choosing an editor (VS Code + LaTeX Workshop), the compile workflow, Overleaf, and using AI carefully.

## Goal

In this first lesson we set up the environment: install TeX, pick an editor, learn the compile workflow, and look at online options (Overleaf) plus how to use AI to speed up writing.

## 1. Local installation (TeX Live)

### 1.1 What is TeX Live?

The most widely used LaTeX distribution. Includes the compiler (pdfTeX, XeTeX, LuaTeX), packages and utilities (bibtex, makeindex, latexmk).

### 1.2 Mac (recommended)

```bash
brew install --cask mactex
```

Verify the install:

```bash
pdflatex --version
latexmk --version
```

> [!warning] Disk space
> TeX Live (MacTeX) takes up 4-5 GB. If you need a smaller install, use `basictex`.

### 1.3 Windows

- **TeX Live**: full installer (recommended if you need many packages).
- **MiKTeX**: installs packages on demand.

### 1.4 Linux

Use your distro's package manager (e.g. `sudo apt install texlive-full` on Ubuntu) or the official installer.

## 2. Recommended editor: Visual Studio Code

- Multi-language support, Git integration.
- The **LaTeX Workshop** extension adds compile-on-save, integrated PDF preview, and error/warning detection.

Recommended `settings.json`:

```json
{
  "latex-workshop.latex.autoBuild.run": "onSave",
  "latex-workshop.latex.outDir": "%DIR%/build",
  "latex-workshop.view.pdf.viewer": "tab"
}
```

## 3. Basic compile workflow

1. Write the `.tex`.
2. Compile (via `latexmk`, VS Code, or Overleaf).
3. Review the PDF.

```bash
latexmk -pdf -interaction=nonstopmode main.tex
```

> [!tip] Tip
> `-interaction=nonstopmode` avoids getting stuck on errors, but always check the log.

## 4. Overleaf (online environment)

No install needed, real-time collaboration, automatic version history — at the cost of compile limits on the free plan and needing a connection.

1. Create an account (Google, GitHub, email).
2. Start a project from a template (article, report, ABNT, etc.).
3. Upload files (`.tex`, `.bib`, images).
4. Compile and view the PDF on the side.

## 5. Using AI with LaTeX (carefully)

- Always ask for output as `.tex` or "LaTeX code".
- Review the result: AI can get commands or syntax wrong.
- Improve the text step by step and keep the original file backed up.

## 🔗 References and related

- [Course overview](en/resource/latex)
- [Lesson 02 — Basics](en/resource/latex/lesson-02-basics)
