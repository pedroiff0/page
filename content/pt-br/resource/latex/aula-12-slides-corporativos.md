---
publish: false
title: "Aula 12 — Slides Corporativos"
created: 2026-07-31
modified: 2026-07-31
tags:
  - latex
  - escrita
  - recursos
  - corporativo
---

> [!note] Resumo
> Construção do tema Beamer `beamerthemecorp.sty`: capa em tela cheia com a cor da marca, título de slide com régua, rodapé com seção e paginação, divisória automática de seção, cartões de KPI, roadmap em TikZ, gráficos na paleta da marca e slide de encerramento. É o par da [Aula 11](pt-br/resource/latex/aula-11-relatorio-corporativo) — **as mesmas seis cores**, agora projetadas em vez de impressas —, e o equivalente corporativo do que a [Aula 09](pt-br/resource/latex/aula-09-slides-beamer) faz com o template institucional do IFF.

**Pré-requisito**: [Aulas 01–05](pt-br/resource/latex) e o básico de Beamer (frames, `\section`, blocos) — a [Aula 09](pt-br/resource/latex/aula-09-slides-beamer) cobre isso na prática. Ler antes a [Aula 11](pt-br/resource/latex/aula-11-relatorio-corporativo) ajuda: a paleta do §2 é literalmente a mesma.

## 0. Tema, não classe — e por quê

A [Aula 09](pt-br/resource/latex/aula-09-slides-beamer) usa uma **classe** (`slidesiffmodelo.cls`, que faz `\LoadClass{beamer}`). Aqui vamos fazer um **tema** (`beamerthemecorp.sty`, usado com `\usetheme{corp}`). A diferença é de acoplamento:

- **Classe** — troca o `\documentclass`. Boa quando o documento é sempre daquele tipo (defesa no campus X, e ponto).
- **Tema** — entra num Beamer comum. Boa quando o mesmo deck pode precisar rodar como `handout`, com outro `aspectratio`, ou com o tema de outro cliente: você troca uma linha, não a classe do documento.

Em contexto corporativo o segundo caso é a regra — cada cliente tem uma marca, e o mesmo conteúdo às vezes é reapresentado com outra identidade. Daí o tema.

O nome do arquivo **não é livre**: `\usetheme{corp}` procura por `beamerthemecorp.sty`. É a mesma convenção de `beamercolortheme...`, `beamerfonttheme...`, `beamerinnertheme...`.

## 1. Esqueleto do tema

```latex
\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{beamerthemecorp}[2026/07/31 v1.0 Tema Beamer corporativo]

\mode<presentation>

\RequirePackage{tikz}
\RequirePackage[most]{tcolorbox}
\RequirePackage{pgfplots}
\pgfplotsset{compat=1.18}
\usetikzlibrary{calc, positioning}

% Opção de tema: \usetheme[escuro]{corp}
\newif\if@corpescuro \@corpescurofalse
\DeclareOptionBeamer{escuro}{\@corpescurotrue}
\ProcessOptionsBeamer
```

`\mode<presentation>` diz ao Beamer que tudo daqui em diante vale só na apresentação — em `\documentclass[handout]` ou ao gerar o artigo (`beamerarticle`), o Beamer sabe o que descartar. Em `.sty` o caractere `@` já é letra, então `\if@corpescuro` funciona sem `\makeatletter`.

## 2. A paleta — idêntica à da Aula 11

```latex
\definecolor{corpPrimaria}{HTML}{123B5C}
\definecolor{corpSecundaria}{HTML}{2E9E8F}
\definecolor{corpDestaque}{HTML}{E8A33D}
\definecolor{corpTexto}{HTML}{1C1C1C}
\definecolor{corpCinza}{HTML}{6B7280}
\definecolor{corpFundo}{HTML}{F4F6F8}

\if@corpescuro
  \setbeamercolor{normal text}{fg=white, bg=corpPrimaria!92!black}
  \setbeamercolor{frametitle}{fg=white}
  \colorlet{corpRegua}{corpSecundaria}
\else
  \setbeamercolor{normal text}{fg=corpTexto, bg=white}
  \setbeamercolor{frametitle}{fg=corpPrimaria}
  \colorlet{corpRegua}{corpSecundaria}
\fi

\setbeamercolor{structure}{fg=corpPrimaria}
\setbeamercolor{title}{fg=white}
\setbeamercolor{subtitle}{fg=white}
\setbeamercolor{itemize item}{fg=corpSecundaria}
\setbeamercolor{itemize subitem}{fg=corpCinza}
\setbeamercolor{enumerate item}{fg=corpSecundaria}
\setbeamercolor{block title}{fg=white, bg=corpPrimaria}
\setbeamercolor{block body}{fg=corpTexto, bg=corpFundo}
\setbeamercolor{block title alerted}{fg=white, bg=corpDestaque}
\setbeamercolor{block body alerted}{fg=corpTexto, bg=corpDestaque!10}
\setbeamercolor{alerted text}{fg=corpDestaque}
\setbeamercolor{section in toc}{fg=corpPrimaria}
\setbeamercolor{footline}{fg=corpCinza, bg=}
```

A variante escura (`\usetheme[escuro]{corp}`) existe por um motivo prático: **auditório com projetor fraco e sala clara pede fundo branco; sala escura e tela grande pede fundo escuro**. Ter as duas no mesmo tema evita manter dois decks.

`\setbeamercolor{footline}{bg=}` com valor vazio é intencional: fundo transparente, herda a cor da página.

## 3. Fontes e proporção de tela

```latex
\usefonttheme{professionalfonts}
\RequirePackage[scaled=0.92]{helvet}
\renewcommand{\familydefault}{\sfdefault}

\setbeamerfont{title}{size=\fontsize{26}{30}\selectfont, series=\bfseries}
\setbeamerfont{subtitle}{size=\normalsize, series=\mdseries}
\setbeamerfont{frametitle}{size=\large, series=\bfseries}
\setbeamerfont{framesubtitle}{size=\footnotesize, series=\mdseries}
\setbeamerfont{footline}{size=\tiny}
\setbeamerfont{block title}{size=\normalsize, series=\bfseries}

\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{caption}[numbered]
\setbeamersize{text margin left=0.9cm, text margin right=0.9cm}
\setlength{\leftmargini}{1.2em}
```

> [!warning] `aspectratio` não pode ficar no tema
> 16:9 se declara na **classe**, não aqui: `\documentclass[aspectratio=169]{beamer}`. O Beamer fixa as dimensões do papel no carregamento da classe; um tema que tentasse mudar isso depois chegaria tarde demais. Sem essa opção você recebe 4:3 — errado para qualquer projetor ou TV atual.

`professionalfonts` impede o Beamer de trocar as fontes matemáticas por conta própria — sem ele, fórmulas ficam com uma sans-serif matemática que não combina com o resto.

## 4. Capa em tela cheia

```latex
\newcommand{\corplogo}{}
\newcommand{\logomarca}[1]{\renewcommand{\corplogo}{#1}}

\defbeamertemplate*{title page}{corp}[1][]{%
  \begin{tikzpicture}[remember picture, overlay]
    \fill[corpPrimaria]
      (current page.north west) rectangle (current page.south east);
    \fill[corpSecundaria]
      ([yshift=2.60cm]current page.south west)
      rectangle ([yshift=2.54cm]current page.south east);

    \node[anchor=south west, text width=0.80\paperwidth, align=left]
      at ([shift={(0.9cm,3.1cm)}]current page.south west) {%
        \usebeamerfont{title}\color{white}\inserttitle\par
        \vspace{0.35cm}
        \usebeamerfont{subtitle}\color{white!80}\insertsubtitle};

    \node[anchor=north west, text width=0.80\paperwidth, align=left]
      at ([shift={(0.9cm,-1.4cm)}]current page.south west) {%
        \footnotesize\color{white!85}
        \insertauthor\par\vspace{2pt}
        \color{white!65}\insertinstitute\par\vspace{2pt}
        \color{white!65}\insertdate};

    \ifx\corplogo\empty\else
      \node[anchor=south east]
        at ([shift={(-0.9cm,0.7cm)}]current page.south east)
        {\includegraphics[height=0.9cm]{\corplogo}};
    \fi
  \end{tikzpicture}}
```

Duas coisas a notar. `\defbeamertemplate*` (com asterisco) **substitui** o template padrão de `title page` — sem o asterisco você só criaria uma variante inativa. E o segundo `\node`, ancorado em `south west` com `yshift` negativo, cai abaixo da faixa: é o bloco de autoria, deliberadamente pequeno — numa capa corporativa o que vende é o título, não quem apresenta.

Como na Aula 11, `remember picture` exige **duas compilações** para posicionar certo.

## 5. Título de slide com régua

```latex
\setbeamertemplate{frametitle}{%
  \nointerlineskip
  \vspace{0.55cm}
  \hspace{0.9cm}%
  \begin{minipage}{0.86\paperwidth}
    \usebeamerfont{frametitle}\usebeamercolor[fg]{frametitle}%
    \insertframetitle\par
    \ifx\insertframesubtitle\@empty\else
      \usebeamerfont{framesubtitle}\color{corpCinza}\insertframesubtitle\par
    \fi
  \end{minipage}\par
  \vspace{0.14cm}
  \hspace{0.9cm}{\color{corpRegua}\rule{0.86\paperwidth}{1.1pt}}
  \vspace{0.10cm}}
```

O teste `\ifx\insertframesubtitle\@empty` é o que permite usar `\framesubtitle` só quando faz sentido, sem deixar um buraco de espaçamento nos slides que não têm subtítulo.

## 6. Rodapé: deck, seção e paginação

```latex
\setbeamertemplate{footline}{%
  \leavevmode
  \hbox{%
    \begin{beamercolorbox}[wd=0.5\paperwidth, ht=2.6ex, dp=1.4ex,
                           leftskip=0.9cm]{footline}
      \usebeamerfont{footline}\insertshorttitle
    \end{beamercolorbox}%
    \begin{beamercolorbox}[wd=0.5\paperwidth, ht=2.6ex, dp=1.4ex,
                           rightskip=0.9cm]{footline}
      \hfill\usebeamerfont{footline}%
      \insertsection\ \textbullet\ \insertframenumber/\inserttotalframenumber
    \end{beamercolorbox}}%
  \vskip2pt}
```

`\inserttotalframenumber` ("slide 7 **de 24**") depende de uma segunda compilação — o total só é conhecido no fim da primeira. Ele merece estar ali: a plateia usa esse número para calibrar paciência.

## 7. Divisória de seção automática

```latex
\AtBeginSection[]{%
  \begin{frame}[plain, noframenumbering]
    \begin{tikzpicture}[remember picture, overlay]
      \fill[corpPrimaria]
        (current page.north west) rectangle (current page.south east);
      \node[anchor=west, text width=0.8\paperwidth, align=left]
        at ([xshift=0.9cm]current page.west) {%
          \color{white!70}\footnotesize\MakeUppercase{Seção \thesection}\par
          \vspace{4pt}
          \color{white}\LARGE\bfseries\insertsectionhead\par
          \vspace{10pt}
          {\color{corpSecundaria}\rule{3.2cm}{2.5pt}}};
    \end{tikzpicture}
  \end{frame}}
```

`\AtBeginSection` dentro do tema é o que torna a divisória **automática**: todo `\section{...}` no deck gera a tela colorida, sem você lembrar de nada. `noframenumbering` mantém a divisória fora da contagem (senão o "de 24" do rodapé inclui telas que não são conteúdo), e `plain` remove cabeçalho e rodapé só dela.

## 8. Cartões de KPI

```latex
\newcommand{\kpi}[3][corpPrimaria]{%
  \begin{tcolorbox}[enhanced, colback=white, colframe=#1, boxrule=1pt,
                    arc=4pt, halign=center, valign=center, height=2.5cm,
                    left=3pt, right=3pt, top=3pt, bottom=3pt]
    {\color{#1}\fontsize{22}{24}\selectfont\bfseries #2}\par\vspace{2pt}
    {\scriptsize\color{corpCinza} #3}
  \end{tcolorbox}}
```

```latex
\begin{frame}{Resultado do trimestre}
  \begin{tcbraster}[raster columns=3, raster equal height,
                    raster column skip=8pt]
    \kpi{+16,1\%}{Receita YoY}
    \kpi[corpSecundaria]{98,4\%}{Disponibilidade}
    \kpi[corpDestaque]{34 dias}{Prazo de recebimento}
  \end{tcbraster}
\end{frame}
```

Um número grande por cartão, um rótulo pequeno, nada mais. O erro clássico do slide de resultado é enfiar o número **dentro** de uma frase — ninguém no fundo da sala lê frase.

## 9. Roadmap em TikZ

```latex
\newcommand{\marco}[4]{%  \marco{posição x}{cor}{data}{rótulo}
  \fill[#2] (#1,0) circle (5pt);
  \node[above=10pt, align=center, font=\scriptsize\bfseries,
        text=corpCinza] at (#1,0) {#3};
  \node[below=10pt, align=center, font=\scriptsize, text width=2.4cm,
        text=corpTexto] at (#1,0) {#4};}
```

```latex
\begin{frame}{Cronograma de implantação}
  \centering
  \begin{tikzpicture}
    \draw[corpCinza!35, line width=2pt] (0,0) -- (11,0);
    \marco{0}{corpPrimaria}{Ago}{Diagnóstico e escopo}
    \marco{3.7}{corpPrimaria}{Set}{Piloto em duas linhas}
    \marco{7.4}{corpSecundaria}{Out}{Expansão}
    \marco{11}{corpDestaque}{Nov}{Revisão de resultados}
  \end{tikzpicture}
\end{frame}
```

Timeline desenhada assim é vetorial, usa a fonte e as cores do deck, e leva menos tempo para ajustar do que arrastar caixas no PowerPoint — que é exatamente o argumento de vender LaTeX para quem não é acadêmico.

## 10. Gráfico e tabela dentro do slide

```latex
\begin{frame}{Receita por linha de produto}
  \centering
  \begin{tikzpicture}
    \begin{axis}[
        ybar, bar width=15pt, width=0.86\paperwidth, height=5.2cm,
        symbolic x coords={Q1,Q2,Q3}, xtick=data,
        ymin=0, enlarge x limits=0.25,
        ymajorgrids, grid style={corpCinza!25},
        axis line style={corpCinza!60},
        tick label style={font=\small, color=corpCinza},
        nodes near coords,
        every node near coord/.append style={font=\scriptsize, color=corpCinza},
        legend style={draw=none, font=\scriptsize, at={(0.5,-0.16)},
                      anchor=north, legend columns=-1}]
      \addplot+[draw=none, fill=corpPrimaria]
        coordinates {(Q1,1240) (Q2,1388) (Q3,1503)};
      \addplot+[draw=none, fill=corpSecundaria]
        coordinates {(Q1,830) (Q2,795) (Q3,910)};
      \legend{Assinaturas, Serviços}
    \end{axis}
  \end{tikzpicture}
\end{frame}
```

Tabela em slide segue outra regra que no relatório: **corte colunas**. Se não couber em 4 colunas e 5 linhas com fonte legível de longe, ela não é um slide — é um anexo.

```latex
\begin{frame}{Comparativo}
  \small
  \begin{tabular}{@{}lrr@{}}
    \toprule
    \textbf{Indicador} & \textbf{Antes} & \textbf{Depois} \\
    \midrule
    Ociosidade (tarde) & 18,0\% & \textbf{7,4\%} \\
    Retrabalho         &  4,2\% & \textbf{2,1\%} \\
    \bottomrule
  \end{tabular}
\end{frame}
```

## 11. Slide de encerramento

```latex
\newcommand{\slidefinal}[2]{%
  \begin{frame}[plain, noframenumbering]
    \begin{tikzpicture}[remember picture, overlay]
      \fill[corpPrimaria]
        (current page.north west) rectangle (current page.south east);
      \node[anchor=west, text width=0.8\paperwidth]
        at ([xshift=0.9cm]current page.west) {%
          \color{white}\Huge\bfseries #1\par
          \vspace{10pt}{\color{corpSecundaria}\rule{3.2cm}{2.5pt}}\par
          \vspace{14pt}\color{white!80}\normalsize #2};
    \end{tikzpicture}
  \end{frame}}
```

```latex
\slidefinal{Obrigado}{pedroiff0@gmail.com \textbullet\ www.phrandrade.com}
```

## 12. `apresentacao.tex` completo

```latex
\documentclass[aspectratio=169, 11pt]{beamer}
\usetheme{corp}          % beamerthemecorp.sty na mesma pasta
% \usetheme[escuro]{corp}  % variante de fundo escuro

\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[brazil]{babel}

\logomarca{figuras/logo-cliente.pdf}

\title{Diagnóstico de Eficiência Operacional}
\subtitle{Resultados do piloto e próximos passos}
\author{Pedro H. R. de Andrade}
\institute{Indústria Exemplo S.A.}
\date{31 de julho de 2026}

\begin{document}

\begin{frame}[plain, noframenumbering]
  \titlepage
\end{frame}

\begin{frame}{Agenda}
  \tableofcontents
\end{frame}

\section{Contexto}
\begin{frame}{O problema em uma tela}
  \framesubtitle{Dados de janeiro a junho de 2026}
  \begin{itemize}
    \item Ociosidade média de \alert{18\%} no turno da tarde.
    \item Concentrada em duas das seis linhas de produção.
  \end{itemize}
\end{frame}

\section{Resultados}
\begin{frame}{Indicadores}
  \begin{tcbraster}[raster columns=3, raster equal height,
                    raster column skip=8pt]
    \kpi{+16,1\%}{Receita YoY}
    \kpi[corpSecundaria]{98,4\%}{Disponibilidade}
    \kpi[corpDestaque]{34 dias}{Prazo de recebimento}
  \end{tcbraster}
\end{frame}

\section{Recomendações}
\begin{frame}{Próximos passos}
  \begin{block}{Recomendação central}
    Remanejar duas equipes do turno da tarde para o turno da manhã.
  \end{block}
  \begin{alertblock}{Risco}
    Depende de renegociação de escala com o sindicato.
  \end{alertblock}
\end{frame}

\slidefinal{Obrigado}{pedroiff0@gmail.com \textbullet\ www.phrandrade.com}

\end{document}
```

## 13. Handout, notas e entrega

```latex
% Um PDF sem overlays, uma página por frame — para imprimir ou enviar por e-mail.
\documentclass[handout, aspectratio=169]{beamer}

% Notas do apresentador na segunda tela (útil com dois monitores):
\setbeameroption{show notes on second screen=right}

% Notas no próprio slide, dentro de qualquer frame:
\note{Lembrar de citar o piloto da linha 3 antes de mostrar o gráfico.}
```

Para gerar o handout **sem tocar no arquivo**, deixe a opção fora e compile com um `main-handout.tex` de duas linhas:

```latex
\PassOptionsToClass{handout}{beamer}
\input{apresentacao.tex}
```

E para 4 slides por folha, `pgfpages`:

```latex
\usepackage{pgfpages}
\pgfpagesuselayout{4 on 1}[a4paper, landscape, border shrink=5mm]
```

## 14. Erros comuns

| Sintoma | Causa | Correção |
|---|---|---|
| Slides em 4:3 | `aspectratio` faltando na classe | `\documentclass[aspectratio=169]{beamer}` (§3) |
| `\usetheme{corp}` não encontrado | nome do arquivo errado | tem que ser `beamerthemecorp.sty` (§0) |
| Capa amontoada no canto | primeira compilação | compilar de novo; use `latexmk -pdf` |
| Rodapé mostra "7/??" | `\inserttotalframenumber` na 1ª passada | compilar de novo |
| Divisória entra na contagem | falta `noframenumbering` | acrescentar em `[plain, noframenumbering]` (§7) |
| Fórmula com fonte estranha | tema de fonte do Beamer | `\usefonttheme{professionalfonts}` (§3) |
| `\alert` sem destaque visível | cor de `alerted text` sobrescrita | conferir `\setbeamercolor{alerted text}` (§2) |
| Frame estourando a tela | conteúdo demais | `\begin{frame}[shrink=10]` — e, de preferência, dividir o slide |

## 🔗 Referências e correlatos

- [Aula 11 — Relatório Corporativo](pt-br/resource/latex/aula-11-relatorio-corporativo) — a mesma paleta em documento impresso.
- [Modelos Corporativos](pt-br/resource/latex/modelos-corporativos) — projeto completo com os dois, e como trocar a marca.
- [Aula 09 — Slides com `slidesiffmodelo.cls`](pt-br/resource/latex/aula-09-slides-beamer) — o equivalente acadêmico, com template institucional do IFF.
- [Modelos de Documento](pt-br/resource/latex/modelos-de-documento) — o Beamer genérico, sem tema próprio.
- [Manual do Beamer](https://ctan.org/pkg/beamer) — a referência dos templates e de `\defbeamertemplate`.
- [Galeria do TikZ](https://texample.net) — ponto de partida para diagramas de slide.
