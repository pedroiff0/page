---
publish: true
title: "Aula 02 — Básico"
created: 2026-03-16
---

> [!note] Resumo
> Estrutura mínima de um documento, listas, alinhamento, figuras, tabelas, equações, classes de documento e os pacotes essenciais.

**Pré-requisito**: [Aula 01](pt-br/resource/latex/aula-01-instalacao) (instalação e ambiente).

## 1. Estrutura mínima de um documento

```latex
\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc} % (não necessário no XeLaTeX/LuaLaTeX)
\usepackage[T1]{fontenc}
\usepackage[brazil]{babel}
\usepackage{lipsum} % texto de exemplo

\title{Título do documento}
\author{Seu Nome}
\date{\today}

\begin{document}
\maketitle
\tableofcontents

\section{Introdução}
\lipsum[1]

\section{Desenvolvimento}
\subsection{Subseção}
\lipsum[2]

\end{document}
```

### 1.1 Sumário automático

- `\tableofcontents` gera automaticamente o índice.
- Use `\section`, `\subsection`, `\subsubsection` para organizar.

## 2. Texto e formatação básica

### 2.1 Listas

```latex
\begin{itemize}
  \item Item simples
  \item Outro item
\end{itemize}

\begin{enumerate}
  \item Primeiro
  \item Segundo
\end{enumerate}
```

### 2.2 Alinhamento

```latex
\begin{flushleft}Texto alinhado à esquerda.\end{flushleft}
\begin{center}Texto centralizado.\end{center}
\begin{flushright}Texto à direita.\end{flushright}
```

## 3. Figuras e tabelas

### 3.1 Inserir figuras

```latex
\usepackage{graphicx}

\begin{figure}[ht]
  \centering
  \includegraphics[width=0.7\textwidth]{exemplo.png}
  \caption{Legenda da figura.}
  \label{fig:exemplo}
\end{figure}
```

### 3.2 Inserir tabelas

```latex
\begin{table}[ht]
  \centering
  \begin{tabular}{|l|c|r|}
    \hline
    Nome & Idade & Nota \\
    \hline
    Ana & 23 & 8.5 \\
    João & 25 & 9.1 \\
    \hline
  \end{tabular}
  \caption{Tabela de exemplo.}
  \label{tab:exemplo}
\end{table}
```

## 4. Equações

```latex
\usepackage{amsmath}

\begin{equation}\label{eq:pitagoras}
  a^2 + b^2 = c^2
\end{equation}
```

Para equações sem numeração, use `\[ ... \]` ou `\begin{equation*}`.

## 5. Classes de documento (quando usar)

- `article`: artigos, relatórios curtos.
- `report`: capítulos, TCCs, trabalhos maiores.
- `book`: livros com capítulos, frontmatter/backmatter.
- `beamer`: apresentações.

> [!tip] Dica
> A classe define comandos como `\chapter` (não disponível em `article`).

## 6. Pacotes essenciais

### 6.1 Pacotes básicos

- `graphicx`: imagens.
- `amsmath`: equações avançadas.
- `hyperref`: links e referências clicáveis.
- `geometry`: margens e tamanho de papel.
- `fontenc`, `inputenc`, `babel`: codificação e idioma (para pdfLaTeX).

### 6.2 Pacotes recomendados para ABNT/TCC

- `abntex2` e `abntex2cite`: normas ABNT.
- `tocloft`: personalizar sumário.
- `biblatex` (ou `natbib`) + `biber` para bibliografia.

## 7. Configurando o documento (preâmbulo)

```latex
\documentclass[12pt,a4paper]{report}
\usepackage[top=3cm,bottom=3cm,left=3cm,right=3cm]{geometry}
\usepackage{setspace}
\doublespacing
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhead[LE,RO]{\thepage}
\fancyhead[LO]{\nouppercase{\rightmark}}
\fancyhead[RE]{\nouppercase{\leftmark}}
```

### 7.1 Fonte e tamanho

Trocar fonte com `fontspec` (XeLaTeX/LuaLaTeX):

```latex
\usepackage{fontspec}
\setmainfont{TeX Gyre Termes}
```

## 🔗 Referências e correlatos

- [Curso — visão geral](pt-br/resource/latex)
- [Aula 01 — Instalação](pt-br/resource/latex/aula-01-instalacao)
- [Aula 03 — Templates e Classes](pt-br/resource/latex/aula-03-modelos)
