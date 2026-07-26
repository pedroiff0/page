---
publish: true
title: Modelos de Documento
created: 2026-03-17
modified: 2026-07-26T11:10:51.519-03:00
published: 2026-07-26T11:10:51.519-03:00
---

> [!note] Resumo
> Estrutura mínima pronta para os tipos de documento mais comuns: Relatório, Livro, Beamer (slides), Pôster científico e o checklist do TCC.

Depois de fazer as [5 aulas do curso](pt-br/resource/latex), use esta página como referência rápida — copie a estrutura mínima e adapte.

## Relatório (`report`)

Para relatórios de disciplina, TCC (antes de migrar para `abntex2`) e trabalhos maiores com capítulos.

```latex
\documentclass[12pt,a4paper]{report}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[brazil]{babel}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{hyperref}

\title{Título do Relatório}
\author{Seu Nome}
\date{\today}

\begin{document}
\maketitle
\tableofcontents

\chapter{Introdução}
Texto da introdução.

\chapter{Metodologia}
Texto da metodologia.

\chapter{Resultados}
Texto dos resultados.

\chapter{Conclusão}
Texto da conclusão.

\end{document}
```

Personalização rápida de cabeçalho:

```latex
\usepackage[top=3cm,bottom=3cm,left=3cm,right=3cm]{geometry}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhead[LE,RO]{\thepage}
\fancyhead[LO]{\nouppercase{\rightmark}}
\fancyhead[RE]{\nouppercase{\leftmark}}
```

## Livro (`book`)

Para material didático com múltiplos capítulos e pré/pós-texto (frontmatter/backmatter).

```latex
\documentclass[12pt,a4paper]{book}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[brazil]{babel}

\title{Título do Livro}
\author{Seu Nome}
\date{\today}

\begin{document}

\frontmatter
\maketitle
\tableofcontents

\mainmatter
\chapter{Primeiro Capítulo}
Texto do capítulo.

\chapter{Segundo Capítulo}
Mais texto.

\backmatter
\chapter{Referências}
\end{document}
```

- `\frontmatter` — numeração romana, sem capítulo numerado.
- `\mainmatter` — numeração arábica, capítulos numerados.
- `\backmatter` — sem numeração de capítulos, uso para bibliografia/apêndices.

## Beamer (apresentações)

```latex
\documentclass{beamer}

\usetheme{Madrid} % tema básico
\usecolortheme{seahorse}

\title{Título da Apresentação}
\author{Seu Nome}
\date{\today}

\begin{document}

\begin{frame}
  \titlepage
\end{frame}

\begin{frame}{Agenda}
  \tableofcontents
\end{frame}

\section{Introdução}
\begin{frame}{Introdução}
  Conteúdo da seção.
\end{frame}

\end{document}
```

Blocos de destaque:

```latex
\begin{frame}{Exemplo de bloco}
  \begin{block}{Título do bloco}
    Texto dentro do bloco.
  \end{block}

  \begin{alertblock}{Alerta}
    Mensagem importante.
  \end{alertblock}
\end{frame}
```

## Pôster científico (`sciposter`)

```latex
\documentclass[a0paper,portrait]{sciposter}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[brazil]{babel}
\usepackage{graphicx}
\usepackage{xcolor}

\title{Título do Pôster}
\author{Seu Nome}
\institute{Instituição}

\begin{document}
\maketitle

\begin{multicols}{2}
  \section{Introdução}
  Texto da introdução.

  \section{Metodologia}
  Texto da metodologia.

  \section{Resultados}
  Texto dos resultados.

  \section{Conclusão}
  Texto da conclusão.
\end{multicols}

\end{document}
```

> [!tip] Dicas rápidas
> Use imagens em alta resolução (PNG/PDF) para não pixelar. Controle o espaçamento com `\vspace`/`\hspace`, e `\columnsep` para o espaço entre colunas. Alternativa com mais controle gráfico: `tikzposter`.

## TCC (checklist ABNT)

O modelo de TCC (via `abntex2`) cobre, entre outros: capa, contracapa, ficha catalográfica, folha de aprovação, agradecimentos, dedicatória, epígrafe, errata, resumo/abstract, listas de ilustrações/tabelas/símbolos, sumário, introdução/metodologia/desenvolvimento/conclusão, referências (ABNT), glossário, apêndices, anexos e índice remissivo — com ambientes próprios para algoritmo, quadro e gráfico, e numeração automática de apêndices/anexos (A, B, C...).

Formatação padrão: Arial 12, justificado, recuo de 1,25 cm, espaçamento uniforme nas seções centralizadas.

## 🔗 Referências e correlatos

- [Curso — visão geral](pt-br/resource/latex)
- [Aula 03 — Templates e Classes](pt-br/resource/latex/aula-03-modelos) — conceitos de classe vs. template.
- [Projeto Final de Curso I](pt-br/resource/engenharia-de-computação/9-periodo/projeto-final-de-curso-i) e [II](pt-br/resource/engenharia-de-computação/10-periodo/projeto-final-de-curso-ii)
- [abnTeX2](https://www.abntex.net.br)
