---
publish: true
title: "Aula 05 — Avançado"
created: 2026-03-16
---

> [!note] Resumo
> Criar pacotes (`.sty`) e classes (`.cls`) próprios, `@makeatletter`, ambientes customizados e compilação avançada.

**Pré-requisito**: [Aulas 01–04](pt-br/resource/latex) (instalação, básico, templates, modularização).

## 1. Criando pacotes (`.sty`)

Um pacote permite compartilhar estilos e comandos entre vários documentos.

```latex
% meuestilo.sty
\ProvidesPackage{meuestilo}[2026/03/17 v1.0]

\RequirePackage{geometry}
\RequirePackage{graphicx}

\newcommand{\meucomando}[1]{\textbf{#1}}

\endinput
```

Use no documento:

```latex
\usepackage{meuestilo}
```

## 2. Criando classes (`.cls`)

Classes são usadas para definir a estrutura do documento (capítulos, margens, comandos padrões).

```latex
% minhaClasse.cls
\ProvidesClass{minhaClasse}[2026/03/17 v1.0]
\LoadClass{article}

\RequirePackage{geometry}
\RequirePackage{titlesec}

\titleformat{\section}{\Large\bfseries}{\thesection}{1em}{}
```

No arquivo principal:

```latex
\documentclass{minhaClasse}
```

## 3. `@makeatletter` e comandos internos

Para acessar comandos internos que usam `@`, use `\makeatletter` / `\makeatother`.

```latex
\makeatletter
\def\@minha@coisa{...}
\makeatother
```

## 4. Criando e reconfigurando ambientes

### 4.1 Redefinindo um ambiente

```latex
\renewenvironment{quote}
  {\begin{center}\itshape}
  {\end{center}}
```

### 4.2 Criando um ambiente novo

```latex
\newenvironment{meuquadro}[1]
  {\begin{center}\fbox{\begin{minipage}{0.9\linewidth}\textbf{#1}\\}}
  {\end{minipage}}\end{center}}
```

## 5. Listas especiais e índices customizados

- `\listoffigures` / `\listoftables` / `\listof{lol}{Título}`
- Criar listas customizadas com `enumitem` ou `tocloft`.

## 6. Compilação avançada

- `latexmk -pdf -pvc` para modo watch (recompila automaticamente).
- `xelatex` / `lualatex` para melhor suporte a Unicode e fontes do sistema.
- `make`, `arara` ou scripts de build para pipelines complexos.

## 🔗 Referências e correlatos

- [Curso — visão geral](pt-br/resource/latex)
- [Aula 04 — Intermediário](pt-br/resource/latex/aula-04-intermediario)
- [Guia de classes (LaTeX Project)](https://www.latex-project.org/help/documentation/clsguide.pdf)
- [CTAN](https://ctan.org/)
