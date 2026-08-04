---
title: "Lecture 09: Resultados e Apresentação Visual de Dados — Slides Institucionais"
publish: true
password: escritaiff2026
created: 2026-08-04
modified: 2026-08-04
tags: [latex, escrita-academica, beamer, pptx, lecture, iff]
---

# Lecture 09: Resultados e Apresentação Visual de Dados
**Curso Profissional de Escrita Acadêmica e LaTeX (80h) — IFF Campus Bom Jesus do Itabapoana**
**Prof. Dr. Pedro Henrique Silva**

> [!IMPORTANT] **Acesso Restrito ao Curso**
> Este recurso de apresentação (**Lecture**) é protegido e exclusivo do curso profissional de Escrita Acadêmica e LaTeX do IFF Campus Bom Jesus do Itabapoana.
> Para consultar o conteúdo teórico detalhado desta lição (Notas de Aula em Português), acesse: **[📝 Notes: Aula 09 — Resultados e Apresentação Visual de Dados](/pt-br/resource/latex/aula-09-resultados-e-apresentacao-de-dados)**.

---

## 1. Apresentação PowerPoint (.pptx) Institucional Widescreen (16:9)

Disponibilizamos o arquivo `.pptx` institucional masterizado nas cores oficiais do campus (**Verde `#2D6238`**, **Vermelho `#B3282D`** e **Cinza `#333333`**), pronto para uso em auditórios, bancas de defesa e seminários do Instituto Federal Fluminense:

> [!TIP] **Download Direto do Slide PPTX Institucional**
> **[📥 Baixar Apresentação PPTX Institucional — Aula 09: Resultados e Apresentação Visual de Dados](/assets/biblioteca/latex-escrita/slides-pptx/aula-09-iff-institucional.pptx)**
> *(Arquivo compatível com Microsoft PowerPoint, LibreOffice Impress e Google Slides)*

### Conversão via Terminal (Pandoc)
Caso deseje converter suas próprias notas Markdown para `.pptx` com a mesma identidade visual:
```bash
pandoc aula-09.md -o aula-09-iff-institucional.pptx --reference-doc=template-iff-widescreen.pptx --slide-level=2
```

---

## Slide Referente da Aula (Beamer — Modelo Institucional IFF)

Abaixo apresentamos o código LaTeX integral dos slides institucionais desta aula, construído com a classe **`slidesiffmodelo.cls`** (na proporção 16:9), integrando automaticamente os metadados oficiais do Instituto Federal Fluminense (IFF):

```latex
\documentclass[aspectratio=169]{slidesiffmodelo}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[brazil]{babel}
\usepackage{amsmath,amssymb}
\usepackage{booktabs}
\usepackage{tikz}

% ==============================================================================
% METADADOS INSTITUCIONAIS - IFF (PROJETO RELATEX)
% ==============================================================================
\titulo{Aula 09: Resultados e Apresentação Visual de Dados (IBGE)}
\subtitulo{Curso Profissional de Escrita Acadêmica e LaTeX (80h)}
\autor{Prof. Dr. Pedro Henrique Silva}
\orientador{Projeto ReLaTeX -- IFF Campus Bom Jesus do Itabapoana}
\curso{Engenharia de Computação / Pós-Graduação}
\campus{Campus Bom Jesus do Itabapoana}
\instituicao{Instituto Federal de Educação, Ciência e Tecnologia Fluminense}
\data{\today}

\begin{document}

% ------------------------------------------------------------------------------
% SLIDE 1: CAPA INSTITUCIONAL IFF
% ------------------------------------------------------------------------------
\begin{frame}[plain]
    \imprimircapa
\end{frame}

% ------------------------------------------------------------------------------
% SLIDE 2: SUMÁRIO E ROTEIRO DA AULA
% ------------------------------------------------------------------------------
\begin{frame}{Roteiro da Aula 09}
    \tableofcontents
\end{frame}

% ------------------------------------------------------------------------------
% SLIDE 3: FUNDAMENTAÇÃO TEÓRICA / NORMATIVA ABNT
% ------------------------------------------------------------------------------
\section{Fundamentação e Normativa}
\begin{frame}{Fundamentação Teórica e Normativa ABNT/IBGE}
    \begin{block}{Diretriz Institucional --- Normas IBGE 1993 vs. Quadros ABNT}
        Tabelas contêm dados quantitativos com laterais abertas; Quadros contêm texto com laterais fechadas.
    \end{block}
    \vspace{0.3cm}
    \textbf{Pontos-Chave da Aula 09:}
    \begin{itemize}
        \item \textbf{Alinhamento Normativo:} Obediência estrita aos padrões canônicos da ABNT e IBGE.
        \item \textbf{Rigor Metodológico:} Regras estritas de legenda no topo e fonte na parte inferior, chamadas no texto antes da figura.
        \item \textbf{Prática em LaTeX:} Automação tipográfica sem intervenção manual de formatação.
    \end{itemize}
\end{frame}

% ------------------------------------------------------------------------------
% SLIDE 4: ARQUITETURA E FLUXO METODOLÓGICO (COLUNAS)
% ------------------------------------------------------------------------------
\section{Arquitetura e Metodologia}
\begin{frame}{Arquitetura de Implementação e Boas Práticas}
    \begin{columns}[c]
        \begin{column}{0.48\textwidth}
            \begin{alertblock}{Atenção Epistemológica}
                Evite desvios normativos ou formatações ad-hoc no código principal. Separe conteúdo de estilo.
            \end{alertblock}
        \end{column}
        \begin{column}{0.48\textwidth}
            \begin{exampleblock}{Padrão Oficial ReLaTeX}
                Utilize as macros centralizadas do pacote \texttt{ifftese.cls} e \texttt{metadados.sty} para manter a conformidade.
            \end{exampleblock}
        \end{column}
    \end{columns}
\end{frame}

% ------------------------------------------------------------------------------
% SLIDE 5: IMPLEMENTAÇÃO NO CÓDIGO (LATEX / ABNT)
% ------------------------------------------------------------------------------
\section{Exemplo Prático (Código)}
\begin{frame}[fragile]{Implementação Prática em LaTeX / ABNT}
    \begin{block}{Snippet de Referência --- Aula 09}
\begin{verbatim}
\begin{table} ... \toprule ... \midrule ... \bottomrule \end{table}
\end{verbatim}
    \end{block}
\end{frame}

% ------------------------------------------------------------------------------
% SLIDE 6: SÍNTESE E REFERÊNCIAS BIBLIOGRÁFICAS
% ------------------------------------------------------------------------------
\section{Síntese e Referências}
\begin{frame}{Síntese da Aula e Referências Normativas}
    \begin{itemize}
        \item Consolidação dos conhecimentos da Aula 09 no ecossistema IFF.
        \item Próxima etapa: Aplicação no arquivo \texttt{metadados.sty} e validação do build.
    \end{itemize}
    \vspace{0.4cm}
    \footnotesize
    \textbf{Referência Principal:}
    \begin{thebibliography}{10}
        \bibitem{ref1} IBGE. Normas de apresentação tabulada. 3. ed. Rio de Janeiro, 1993.
    \end{thebibliography}
\end{frame}

\end{document}
```

---

## 🔗 Navegação da Aula
- **[📝 Voltar para as Notas de Aula (Notes): Aula 09](/pt-br/resource/latex/aula-09-resultados-e-apresentacao-de-dados)**
- **[🏠 Voltar para o Portal Principal do Curso](/pt-br/resource/latex/)**
