---
publish: false
title: "Aula 09 — Slides com slidesiffmodelo.cls"
created: 2026-07-26
modified: 2026-07-26
tags:
  - latex
  - escrita
  - recursos
---

> [!note] Resumo
> `slidesiffmodelo.cls` é o template oficial de slides do IFF Campus Bom Jesus do Itabapoana, usado em eventos como a Mostra do Conhecimento e Feira de Oportunidades — a mesma classe que usei para apresentar [Detecção de Anomalias em Dados do Gaia](pt-br/research/anomaly-detection). É um `\LoadClass{beamer}` por baixo, então tudo que você já sabe de Beamer continua valendo, mas com layout, cabeçalho/rodapé com logos e macros de figura já resolvidos pela classe — igual ao raciocínio já aplicado ao pôster ([Aula 10](pt-br/resource/latex/aula-10-poster-cientifico)). O [modelo baixável](#-modelo-completo-preenchido) abaixo usa o conteúdo científico real desse trabalho (mesmos gráficos e resultados do pôster), com título/autores deixados como campos de exemplo para reuso.

**Pré-requisito**: [Aulas 01–05](pt-br/resource/latex) (básico, classes de documento, `\documentclass`/pacotes). Útil ter visto [Aula 06](pt-br/resource/latex/aula-06-classe-ifftese) — `slidesiffmodelo.cls` reaproveita os mesmos atalhos de notação (`\feh`, `\mgfe`...) e abreviações de periódico da mesma "família" de classes, mas é independente: não carrega `ifftese.cls`, só o `beamer` padrão.

**Ver também**: [Aula 10 — Pôster Científico com `iffposter.cls`](pt-br/resource/latex/aula-10-poster-cientifico) — o mesmo raciocínio de "resumo visual do trabalho com template institucional pronto", em formato de banner impresso em vez de slides projetados.

## 0. Por que um documento separado do TCC

Slides de defesa não são "o TCC reformatado" — são um **resumo visual** dele, com muito menos texto por página e ênfase em figuras/gráficos grandes. Por isso os slides são um projeto LaTeX independente: `\documentclass{slidesiffmodelo}` num arquivo à parte, copiando manualmente só os poucos dados que os slides realmente precisam (título, autores, instituição), sem depender da infraestrutura de metadados de `ifftese.cls`.

```latex
\documentclass[10pt, aspectratio=169]{slidesiffmodelo}
\usepackage{metadados}

\title{Título do Trabalho: subtítulo do trabalho}
\author{Nome do Autor\inst{1}}
\institute{\inst{1} Instituto Federal Fluminense \textit{Campus} Bom Jesus do Itabapoana}

\begin{document}
\begin{frame}[t]
  \titlepage
\end{frame}
\end{document}
```

`aspectratio=169` é a opção mais importante a lembrar: sem ela, o Beamer assume 4:3 por padrão — errado para qualquer monitor/projetor atual. `metadados.sty` aqui é **um arquivo diferente** do `metadados.sty` da Aula 08, mesmo nome, propósito distinto — só configura header/footer/logos dos slides, não dados de banca/TCC.

## 1. A classe herda de `beamer`, não o substitui

```latex
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{slidesiffmodelo}[2026/05/30 Modelo de Slides IFF - Padrão CONFICT]

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{beamer}}
\ProcessOptions\relax
\LoadClass{beamer}
```

Mesmo padrão de `iffposter.cls` (que herda `extarticle`): qualquer opção que você passar em `\documentclass[opção]{slidesiffmodelo}` — como `10pt` ou `aspectratio=169` do exemplo acima — é simplesmente repassada para `beamer` via `\DeclareOption*`, sem a classe precisar conhecer cada opção possível do Beamer de antemão.

## 2. Atalhos de notação e bibliografia (mesma família de `ifftese.cls`/`iffposter.cls`)

```latex
\newcommand{\feh}{[Fe/H]}
\newcommand{\mgfe}{[Mg/Fe]}
\newcommand{\teff}{$T_{\text{eff}}$}
\newcommand{\logg}{$\log g$}
\newcommand{\estrela}{$\bigstar$s }
```

Mesmos atalhos de [Aula 10 §2](pt-br/resource/latex/aula-10-poster-cientifico) (menos `\sel`, que essa classe não declara), direto na classe pelo mesmo motivo: slides não têm "metadados do estudante" para ficarem num arquivo de preenchimento à parte. A bibliografia usa o mesmo `abntex2cite` das outras duas classes (`[alf, abnt-etal-text=it, abnt-emphasize=bf, abnt-etal-list=4, abnt-etal-cite=4]`) e o mesmo bloco de ~15 abreviações de periódico de astronomia (`\aap`, `\mnras`, `\apj`...).

## 3. Neutralização de cores — igual filosofia das bordas invisíveis de `ifftese.cls`

```latex
\setbeamercolor{normal text}{fg=black,bg=white}
\setbeamercolor{structure}{fg=black}
\setbeamercolor{title}{fg=black}
\setbeamercolor{frametitle}{fg=black}
\setbeamercolor{item}{fg=black}
\setbeamercolor{caption}{fg=black}
\setbeamercolor{caption name}{fg=black}
```

A maioria dos temas do Beamer (`Madrid`, `Berlin`...) vem com uma cor de destaque forte por padrão. Aqui a classe zera tudo para preto sobre branco — decisão de design equivalente à das bordas de link brancas em `ifftese.cls` (Aula 06 §2.3): um documento sóbrio, que não depende de cor para ser legível quando impresso ou projetado num equipamento ruim. Cor entra só via imagens de cabeçalho/logos (§6), não via tema do Beamer.

## 4. Margens, espaçamento de lista e símbolos de navegação

```latex
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{frametitle continuation}{}
\usefonttheme{professionalfonts}

\setbeamersize{text margin left=0.4cm, text margin right=0.4cm}

\setlength{\leftmargini}{1.1em}
\setlength{\leftmarginii}{1.0em}
\setlength{\leftmarginiii}{1.0em}

\addtobeamertemplate{itemize/enumerate body begin}{\vspace*{-2pt}}{}
\addtobeamertemplate{itemize/enumerate body end}{\vspace*{-2pt}}{}
\addtobeamertemplate{itemize i}{\setlength{\itemsep}{2pt}\setlength{\topsep}{0pt}\setlength{\parsep}{0pt}}{}
```

`navigation symbols` some (a barrinha de setinhas que o Beamer desenha por padrão no rodapé — inútil numa defesa apresentada com clicker, e visualmente poluída). As margens de texto ficam bem apertadas (0,4cm) porque a classe já reserva espaço fixo para cabeçalho/rodapé de imagem (§6) — sobra pouco espaço vertical/horizontal útil, então o resto é otimizado ao máximo. O espaçamento entre itens de lista é reduzido (`itemsep`/`topsep`/`parsep` próximos de zero) pelo mesmo motivo: cada frame tem pouquíssima altura disponível.

## 5. As chaves de frame `[img]`/`[small]` — herança automática de tamanho de fonte

```latex
\newif\if@imgframe \@imgframefalse
\newif\if@smallframe \@smallframefalse

\define@key{beamerframe}{img}[true]{\global\@imgframetrue}
\define@key{beamerframe}{small}[true]{\global\@smallframetrue}

\addtobeamertemplate{frame begin}{}{%
    \if@imgframe \global\@smallframetrue \fi
    \if@smallframe
        \scriptsize
        \setbeamerfont{section in toc}{size=\scriptsize}
        \setbeamerfont{bibliography item}{size=\scriptsize}
        % ... demais fontes do sumário/bibliografia
    \fi
}
\addtobeamertemplate{frame end}{}{%
    \if@smallframe \normalsize \global\@smallframefalse \global\@imgframefalse \fi
}
```

`\define@key{beamerframe}{...}` registra **duas opções customizadas** que passam a existir dentro dos colchetes de qualquer `\begin{frame}[...]`, ao lado das opções nativas do Beamer (`t`, `allowframebreaks`...). `\begin{frame}[img]` ativa automaticamente `\scriptsize` (via `\@imgframetrue` implicando `\@smallframetrue`) para todo o frame — a lógica por trás é que um frame com imagem grande sobra pouco espaço de texto, então a classe já assume fonte pequena sem você precisar lembrar de forçar manualmente. `\begin{frame}[small]` faz só a parte da fonte pequena, sem a suposição de imagem. Os `\if@smallframe`/`\if@imgframe` são resetados (`\global...false`) no `frame end`, então o efeito nunca "vaza" para o próximo frame.

## 6. Ambiente `textoimagem` — duas colunas com herança de fonte

```latex
\newenvironment{textoimagem}{%
    \begin{columns}[T, onlytextwidth]
    \begin{column}{0.4\textwidth}
        \if@smallframe \scriptsize \fi
}{%
    \end{column}
    \end{columns}
}

\newcommand{\colunaimagem}{%
    \end{column}
    \begin{column}{0.58\textwidth}
        \vspace*{-0.6cm}
        \if@smallframe \scriptsize \fi
}
```

Padrão de layout mais usado no modelo: texto (40% da largura) à esquerda, imagem (58%) à direita, com um `\colunaimagem` no meio trocando de coluna. `[T, onlytextwidth]` alinha as duas colunas pelo topo e faz `\textwidth` dentro de cada `column` valer a largura real da coluna (não a largura total da página, que é o comportamento padrão confuso do ambiente `columns` do Beamer). Cada metade repete `\if@smallframe \scriptsize \fi` — necessário porque abrir uma nova `column` reresetaria o tamanho de fonte para o padrão do Beamer se a classe não reforçasse a flag manualmente nos dois pontos.

Uso típico (do `main.tex` do modelo):

```latex
\begin{frame}[t, allowframebreaks, small]
    \frametitle{Contexto}
    \begin{textoimagem}
        \begin{itemize}
            \item Telescópios de grande porte;
            \item \textit{Big Data};
        \end{itemize}
    \colunaimagem
        \inserirfigura[width=0.8\linewidth]{img/gaia.jpg}{Satélite \emph{Gaia}, da ESA}{}{fig:gaia}
    \end{textoimagem}
\end{frame}
```

## 7. Cabeçalho, rodapé com até 3 logos e capa automatizada

```latex
\setbeamertemplate{headline}{
    \ifx\@headerimg\empty\else
        \begin{beamercolorbox}[wd=\paperwidth, ht=\@headerheight, dp=0cm]{}
            \includegraphics[width=\paperwidth, height=\@headerheight, keepaspectratio=false]{\@headerimg}
        \end{beamercolorbox}
    \fi
}

\setbeamertemplate{footline}{
\ifx\@footerimgA\empty\else
    \begin{beamercolorbox}[wd=\paperwidth, ht=\@footerheight, dp=0cm, center]{}
        \makebox[\paperwidth][c]{%
            \raisebox{0.1cm}{\includegraphics[height=\@footerheight, keepaspectratio]{\@footerimgA}}%
            \ifx\@footerimgB\empty\else\hspace{0.25cm}\includegraphics[...]{\@footerimgB}\fi
            \ifx\@footerimgC\empty\else\hspace{0.25cm}\includegraphics[...]{\@footerimgC}\fi
        }%
    \end{beamercolorbox}
\fi
}
```

`\setheaderimage{arquivo}` estampa uma imagem de largura total no topo de **todo frame** (o cabeçalho do evento — no modelo, `capa/cabecalho.jpg`); `\setfooterimgs{A}{B}{C}` aceita até três logos de rodapé (no modelo, FAPERJ/CNPq/cabeçalho pequeno do campus), cada um opcional e testado individualmente com `\ifx...\empty`. `\setheaderheight`/`\setfooterheight` controlam a altura reservada — a classe usa `beamercolorbox` (não `\includegraphics` solto) porque isso garante que a caixa reserve exatamente a altura declarada mesmo antes da imagem carregar, evitando que o layout "pule" durante a compilação.

A capa (`title page`) desenha três colunas — logos à esquerda, título/autor/instituição ao centro, logos à direita — o mesmo esquema de três colunas de logo usado no `\maketitle` de `iffposter.cls` (Aula 10 §7), só que mais simples (sem o cálculo dinâmico de largura quando um lado não tem logo):

```latex
\setbeamertemplate{title page}{
    \begin{center}
        {\large \textbf{\inserttitle}\par}
        {\normalsize \insertauthor\par}
        {\scriptsize \insertinstitute\par}
    \end{center}
    \vfill
    \begin{minipage}[b]{\textwidth}
        \begin{minipage}[c]{0.3\textwidth}\centering\ifx\@logoEsq\empty\else\@logoEsq\fi\end{minipage}\hfill
        \begin{minipage}[c]{0.3\textwidth}\centering\ifx\@logoMeio\empty\else\@logoMeio\fi\end{minipage}\hfill
        \begin{minipage}[c]{0.3\textwidth}\centering\ifx\@logoDir\empty\else\@logoDir\fi\end{minipage}
    \end{minipage}
}
```

## 8. `\inserirfigura`/`\inserirtabela` — terceira assinatura diferente

```latex
\newcommand{\inserirfigura}[5][width=\linewidth]{
    \begin{figure}[H]
        \vspace*{-0.2cm}
        \caption{#3}
        \centering
        \includegraphics[height=0.78\textheight, keepaspectratio, #1]{#2}
        \label{#5}
        \imprimirfonte{#4}
        \vspace*{-0.2cm}
    \end{figure}
}
```

> [!warning] Terceira assinatura diferente — não confundir com Aula 07 nem Aula 10
> Cada classe da "família" ABNT/IFF-BJI define seu próprio `\inserirfigura`, com ordem de argumentos própria:
> - `ifftese.cls` (Aula 07): `[opções]{arquivo}{legenda-longa}{legenda-curta}{fonte}{label}` — 6 posições, com legenda curta (Lista de Figuras).
> - `iffposter.cls` (Aula 10): `[largura]{arquivo}{legenda}{fonte}{label}` — 5 posições, sem legenda curta.
> - `slidesiffmodelo.cls` (aqui): `[opções={height=...,width=...}]{arquivo}{legenda}{fonte}{label}` — 5 posições como o pôster, mas o argumento opcional aceita chaves de `\includegraphics` inteiras (`height`/`width`/`keepaspectratio`), não só uma largura, e o `\caption` é montado **antes** do `\includegraphics` no código (a ordem de renderização na página não muda — legenda continua no topo, por causa de `\captionsetup{position=top}` no §9 abaixo).
>
> Usar a assinatura errada num documento que carrega a classe errada gera erro de compilação ou, pior, texto no lugar errado sem erro nenhum.

`\imprimirfonte{#4}` só imprime a linha "Fonte: ..." se o 4º argumento não estiver vazio (`\ifstrempty`) — mesmo padrão dos floats condicionais de `ifftese.cls`. `\inserirtabela` segue o mesmo espírito, recebendo o conteúdo da tabela pronto como argumento (`#3`, tipicamente um `tabular`/`tabularx`).

## 9. Legendas pequenas e no topo

```latex
\setbeamertemplate{caption}[numbered]
\captionsetup{font=scriptsize, labelfont=bf, justification=centering, singlelinecheck=false, position=top, skip=0pt}
```

`position=top` é o motivo de `\caption{#3}` aparecer antes do `\includegraphics` no código do §8 — em slides a legenda funciona melhor como título da figura (lida primeiro, junto com o resto do texto do frame) do que como rodapé, ao contrário do padrão de livro/artigo. Fonte reduzida (`scriptsize`) porque a legenda compete por espaço vertical com o resto do conteúdo do frame, que já é escasso.

## 10. Estrutura do `main.tex` do modelo

```latex
\begin{frame}[t,small]
    \frametitle{Sumário}
    \small
    \tableofcontents[hideallsubsections,sectionstyle=show]
\end{frame}

\section{Introdução}
\subsection{Contexto}
\begin{frame}[t, allowframebreaks, small]
    \frametitle{Contexto}
    ...
\end{frame}
```

`\tableofcontents[hideallsubsections,sectionstyle=show]` mostra só as `\section`s no sumário inicial (as `\subsection`s existem só para marcar sub-tópicos internamente, sem poluir a visão geral). `allowframebreaks` deixa um frame "vazar" para uma segunda página automaticamente se o conteúdo não couber — útil combinado com `[img]`/`[small]`, já que é comum um frame com imagem grande precisar de mais espaço do que cabe numa tela 16:9. A seção final de referências usa o mesmo recurso:

```latex
\section*{Referências}
\begin{frame}[allowframebreaks]
    \frametitle{Referências}
    \bibliography{referencias}
\end{frame}
```

`\section*` (com asterisco) não numera nem entra no sumário — usado tanto para "Agradecimentos" quanto para "Referências", que são seções de fechamento, não conteúdo do trabalho em si.

## 11. Compilação

```
pdflatex main
pdflatex main   % 2ª passada: sumário e numeração de seção
bibtex main     % só se houver \cite/\citeonline no texto
pdflatex main
pdflatex main
```

Funciona em qualquer distribuição LaTeX moderna ou no Overleaf.

---

## 📦 Modelo completo preenchido

**[Baixar modelo-slide-iffbji.zip](assets/biblioteca/latex-escrita/modelo-slide-iffbji.zip)** — não é um exemplo genérico: usa o conteúdo científico real do mesmo trabalho descrito em [Detecção de Anomalias em Dados do Gaia](pt-br/research/anomaly-detection), com o cabeçalho oficial do evento e os logos de fomento (FAPERJ/CNPq) inclusos — introdução, catálogos utilizados (Gaia GCNS, GALAH DR4), objetivos, metodologia, os mesmos 4 gráficos de resultado do pôster (Kiel, Toomre, Tinsley-Wallerstein, [Fe/H]–[Mg/Fe]) e conclusões. Título e segundo autor ficam como campos de exemplo, prontos para você substituir pelos seus. Compilado e verificado antes de publicar.

---

## 🔗 Referências e correlatos

- [Aula 06 — Classe `ifftese.cls`](pt-br/resource/latex/aula-06-classe-ifftese) — origem dos atalhos de notação (`\feh`/`\mgfe`) e da filosofia de cores neutras reaproveitados aqui.
- [Aula 10 — Pôster Científico com `iffposter.cls`](pt-br/resource/latex/aula-10-poster-cientifico) — a classe "irmã" para o formato impresso, com vários padrões em comum (logos, `\inserirfigura`, bibliografia).
- [ReLaTeX — pesquisa por trás da classe `ifftese.cls`](pt-br/research/relatex) — o projeto que originou toda essa família de classes do IFF-BJI.
- [Detecção de Anomalias em Dados do Gaia](pt-br/research/anomaly-detection) — a pesquisa por trás destes slides.
- [Metodologia Científica e Tecnológica](pt-br/resource/engenharia-de-computação/8-periodo/metodologia-cientifica-e-tecnologica) — onde entra a preparação para apresentar um trabalho em banca/evento.
- [Projeto Final de Curso I](pt-br/resource/engenharia-de-computação/9-periodo/projeto-final-de-curso-i) e [II](pt-br/resource/engenharia-de-computação/10-periodo/projeto-final-de-curso-ii)
- [Documentação oficial do Beamer (CTAN)](https://ctan.org/pkg/beamer)
- [Curso — visão geral](pt-br/resource/latex)
