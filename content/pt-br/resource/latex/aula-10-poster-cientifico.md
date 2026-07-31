---
publish: false
title: Aula 10 — Pôster Científico com iffposter.cls
created: 2026-07-26
modified: 2026-07-26T23:54:06.103-03:00
published: 2026-07-26T23:54:06.103-03:00
tags:
  - latex
  - escrita
  - recursos
---

> [!note] Resumo
> `iffposter.cls` é a classe oficial usada em pôsteres do IFF Campus Bom Jesus do Itabapoana — a mesma que usei para levar meu próprio trabalho (Etapa 1 de [Detecção de Anomalias em Dados do Gaia](pt-br/research/anomaly-detection)) à **XIV Mostra do Conhecimento e VII Feira de Oportunidades** do campus. Documento aqui cada flag/comando dela, e o [modelo baixável](#-modelo-completo-preenchido) abaixo é esse pôster real, não um exemplo fictício.

**Pré-requisito**: [Aulas 01–05](pt-br/resource/latex) (básico, classes de documento). Útil ter visto [Aula 06](pt-br/resource/latex/aula-06-classe-ifftese) — `iffposter.cls` reaproveita vários padrões da mesma "família" de classes (atalhos `\feh`/`\mgfe`, abreviações de periódicos, `abntex2cite`), mas é uma classe **independente**, não carrega `ifftese.cls`.

## 0. Arquitetura: dois arquivos, não três

Mais simples que o trio da classe de TCC — aqui são só dois:

| Arquivo | Papel |
|---|---|
| `iffposter.cls` | O motor: layout, cores, cabeçalho/rodapé com imagem, sistema de logos, `\inserirfigura`/`\inserirtabela` |
| `metadados.sty` | Preenchimento: tamanhos, cores, cabeçalho/rodapé, logos — **um arquivo diferente** do `metadados.sty` da Aula 08, mesmo nome, propósito distinto |

```latex
\documentclass[]{iffposter}
\usepackage{metadados}

\title{Título do trabalho}
\author{Nome do Autor\inst{1}}
\institute{\inst{1} Instituto Federal Fluminense \textit{Campus} Bom Jesus do Itabapoana}

\begin{document}
\maketitle
\begin{multicols*}{2}
  \section{Introdução}
  ...
\end{multicols*}
\end{document}
```

## 1. Opção de classe: `maior`

```latex
\newif\if@posterMaior \@posterMaiorfalse
\DeclareOption{maior}{\@posterMaiortrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{extarticle}}
\ProcessOptions\relax
\LoadClass[20pt]{extarticle}
```

A classe herda de `extarticle` (variante do `article` com mais tamanhos de fonte disponíveis), sempre carregada a 20pt — forçado mesmo se você não passar nenhuma opção, para evitar que `extarticle` caia silenciosamente para 10pt. A opção `maior` liga um `\newif` que **reconfigura toda a escala do documento de uma vez** — ver §5. Qualquer outra opção passada (`\DeclareOption*`) é repassada direto para `extarticle`.

## 2. Atalhos de notação (idênticos aos de `ifftese.cls`)

```latex
\newcommand{\feh}{[Fe/H]}
\newcommand{\mgfe}{[Mg/Fe]}
\newcommand{\teff}{$T_{\text{eff}}$}
\newcommand{\logg}{$\log g$}
\newcommand{\sel}{s$^{-1}$}
\newcommand{\estrela}{$\bigstar$s }
```

Exatamente os mesmos seis atalhos declarados em `metadados.sty` da Aula 08 (mesmo autor, mesma convenção de notação) — aqui, porém, ficam direto na classe, não num arquivo de preenchimento separado, porque um pôster não tem "metadados do estudante" no mesmo sentido de um TCC.

## 3. Bibliografia: `abntex2cite` + abreviações de periódicos

```latex
\RequirePackage[alf, abnt-emphasize=bf, abnt-etal-list=4, abnt-etal-text=emph]{abntex2cite}
\def\aj{AJ} \def\araa{ARA\&A} \def\apj{ApJ} ...
```

Mesmo pacote de citação ABNT da Aula 06, com um subconjunto menor de opções (só o essencial para citação em pôster: negrito no autor, "et al." a partir de 4 autores). As abreviações de periódico (`\aj`, `\mnras`, `\aap`...) são as mesmas siglas curtas usadas em BibTeX no estilo AASTeX.

## 4. Sistema de cores

```latex
\definecolor{PosterGreen}{RGB}{31,117,80}
\colorlet{mainCol}{white}    % fundo do pôster
\colorlet{TextCol}{black}    % texto geral
\colorlet{BoxCol}{PosterGreen}  % caixa das seções
\colorlet{SectionCol}{white}    % texto dentro da caixa de seção

\newcommand{\setSectionBoxColor}[1]{\colorlet{BoxCol}{#1}}
\newcommand{\setSectionTextColor}[1]{\colorlet{SectionCol}{#1}}
\newcommand{\setBgColor}[1]{\colorlet{mainCol}{#1}}
\newcommand{\setTextColor}[1]{\colorlet{TextCol}{#1}}
```

Quatro variáveis de cor (`\colorlet`, não `\definecolor` — permite apontar para qualquer cor já definida, inclusive uma seguinte) mais quatro comandos de conveniência para trocá-las em `metadados.sty` sem precisar saber `\colorlet` existe. Testado, funciona com qualquer nome de cor do `xcolor` (nomes puros como `white`/`black`, ou uma cor customizada como `PosterGreen`).

## 5. Escala dinâmica: normal vs. `maior`

O bloco mais importante da classe — uma única flag (`\if@posterMaior`) reconfigura **simultaneamente** tamanho de fonte, dimensões de cabeçalho/rodapé e tamanho físico do papel:

```latex
\if@posterMaior
    \renewcommand{\normalsize}{\fontsize{25}{30}\selectfont}
    \renewcommand{\Huge}{\fontsize{65}{75}\selectfont}
    \setlength{\headerH}{10cm}
    \settitlefont{\fontsize{65}{75}\bfseries}
    \geometry{paperwidth=90cm, paperheight=120cm}
\else
    \setlength{\headerH}{5cm}
    \settitlefont{\huge\bfseries}
    \geometry{paperwidth=70cm, paperheight=100cm}
\fi
```

Sem `maior`: pôster "menor" (70×120cm), com fontes relativas padrão (`\huge`, `\Large`...). Com `maior`: reescreve `\normalsize` até `\Huge` para tamanhos absolutos em pontos (via `anyfontsize`, que permite qualquer `\fontsize` sem estar limitado à tabela padrão de tamanhos do LaTeX) e infla o papel para 90×120cm — o tamanho A0-like usual de congresso. `\settitlefont`/`\setauthorfont`/`\setinstfont`/`\setbibfont` (comandos de conveniência, só `\renewcommand` de macros vazias) recebem valores coerentes com a escala escolhida em cada ramo.

> [!tip] Diferença do modelo baixável
> O [modelo completo](#-modelo-completo-preenchido) usa `\documentclass[]{iffposter}` (preset menor, 70×100cm) — troque para `\documentclass[maior]{iffposter}` se seu evento pedir A0 (90×120cm) de verdade.

## 6. Cabeçalho e rodapé com imagem

```latex
\newcommand{\setheader}[1]{\renewcommand{\@headerimg}{#1}}
\newcommand{\setfooterimgs}[3]{\def\@footerimgA{#1}\def\@footerimgB{#2}\def\@footerimgC{#3}}
\newcommand{\noheader}{\@showheaderfalse}
\newcommand{\nofooter}{\@showfooterfalse}
```

`\setheader{arquivo}` estampa uma imagem de largura total no topo da página (o banner do evento, no modelo baixável: `capa/cabecalho.jpg` — "XIV Mostra do Conhecimento e VII Feira de Oportunidades"). `\setfooterimgs{A}{B}{C}` aceita **até três** imagens de rodapé (logos de fomento — FAPERJ, CNPq, o cabeçalho do campus), cada uma opcional (`\ifdefempty` testa cada uma individualmente):

```latex
\AtPageLowerLeft{\put(\footerOffset, \footerOffset){%
  \parbox[b][\@tmpFHeight][c]{\@tmpFWidth}{%
    \hspace*{\fill}
    \includegraphics[height=\@tmpFHeight]{\@footerimgA}
    \ifdefempty{\@footerimgB}{}{\hfill\includegraphics[height=\@tmpFHeight]{\@footerimgB}}
    \ifdefempty{\@footerimgC}{}{\hfill\includegraphics[height=\@tmpFHeight]{\@footerimgC}}
    \hspace*{\fill}
  }%
}}
```

O truque de layout: `\hspace*{\fill}...\hfill...\hfill...\hspace*{\fill}` cria espaço elástico **antes, entre e depois** das imagens presentes — não importa se você define uma, duas ou três, elas sempre ficam centralizadas como grupo, com espaçamento uniforme entre si. `\AddToShipoutPictureBG*` desenha isso no _background_ da página (atrás do conteúdo), e a classe recalcula a área útil de texto (`\newgeometry` com `top`/`bottom` dependendo de `\headerH`/`\footerH`) automaticamente, para o texto nunca invadir essas faixas.

## 7. Sistema de logos e `\maketitle`

```latex
\newcommand{\lefttoplogo}[2][0.9]{\renewcommand{\@ltscale}{#1}\renewcommand{\@lefttoplogo}{#2}}
\newcommand{\nolefttoplogo}{\renewcommand{\@lefttoplogo}{}}
```

Quatro posições possíveis (`lefttoplogo`/`righttoplogo`/`leftbottomlogo`/`rightbottomlogo`), cada uma com um comando `\set...` que aceita uma **escala opcional** entre colchetes (`\lefttoplogo[1.0]{arquivo}`) e um `\no...` para desativar. `\maketitle` é redefinido para desenhar **três colunas**: logos à esquerda, título/autores/instituição ao centro, logos à direita —

```latex
\ifdefempty{\@lefttoplogo}{\ifdefempty{\@leftbottomlogo}{\def\@leftwidth{0}}{}}{}
\pgfmathsetmacro{\@midwidth}{1 - \@leftwidth - \@rightwidth}
```

Se um dos lados não tiver **nenhuma** logo (nem superior nem inferior), sua largura vira `0` e a coluna central absorve o espaço — o título fica automaticamente centralizado na largura total, sem colunas fantasmas vazias. `\IfFileExists` protege cada `\includegraphics` (se o arquivo de logo não existir, simplesmente não desenha nada em vez de dar erro de compilação).

## 8. `\section` como caixa colorida

```latex
\RenewDocumentCommand{\section}{s m}{
  \begin{tcolorbox}[colback=BoxCol, colframe=BoxCol, coltext=SectionCol, arc=5mm, ...]
    \IfBooleanTF{#1}{#2}{\thesection.\hspace{0.5em}#2}
  \end{tcolorbox}
}
```

`\RenewDocumentCommand` (do pacote `xparse`, mais expressivo que `\renewcommand`) declara a assinatura `s m` — **s**tar opcional + **m**andatório — permitindo tanto `\section{Título}` (numerado: "1. Título") quanto `\section*{Título}` (sem número). Cada seção vira uma caixa `tcolorbox` com cantos arredondados (`arc=5mm`) na cor `BoxCol`/`SectionCol` configurada em `metadados.sty` — bem diferente do `\section` sóbrio (texto simples, sem caixa) usado em `ifftese.cls`.

## 9. `\inserirfigura`/`\inserirtabela` — assinatura diferente da Aula 07

```latex
\newcommand{\inserirfigura}[5][0.9\columnwidth]{
  \captionof{figure}{#3}
  \label{#5}
  \includegraphics[width=#1]{#2}
  \ifstrempty{#4}{}{\textbf{Fonte:} #4}
}
```

> [!warning] Não confundir com `\inserirfigura` da Aula 07
> Mesmo nome, **classe diferente, argumentos em ordem diferente**. Em `ifftese.cls` (TCC): `[opções]{arquivo}{legenda-longa}{legenda-curta}{fonte}{label}` — 6 posições. Aqui, em `iffposter.cls`: `[largura]{arquivo}{legenda}{fonte}{label}` — 5 posições, sem legenda curta (pôster não tem "Lista de Figuras"). Usar a ordem errada em um documento que carrega a outra classe gera erro de compilação ou, pior, texto no lugar errado sem erro nenhum.

Uso no modelo: `\inserirfigura[\columnwidth]{img/SBPC_Fig1_Feh_MgFe.pdf}{legenda}{fonte}{fig:feh_mgfe}`. `\inserirtabela` segue o mesmo espírito, com `\begin{tabular}{colunas}...\end{tabular}` como argumento de conteúdo entre `\toprule`/`\bottomrule` fixos.

## 10. Bibliografia com fonte reduzida

```latex
\let\OLDthebibliography\thebibliography
\renewcommand\thebibliography[1]{
  \OLDthebibliography{#1}
  \@bibfont
  \vspace{-1.0em}
  \setlength{\itemsep}{-0.2em}
}
```

Salva a implementação original (`\let\OLDthebibliography\thebibliography`) e a chama primeiro, só então aplicando a fonte reduzida (`\@bibfont`, configurada em `metadados.sty` — ex. `\small`) e um espaçamento negativo entre itens, para a lista de referências caber em pôster sem dominar visualmente a última coluna. Mesmo padrão de "decorar o original em vez de reescrever do zero" usado por `\thebibliography` em `ifftese.cls` (Aula 06 §6), mais simples aqui (sem os labels `refInicio`/`refFim`, que só fazem sentido numa ficha catalográfica).

---

## 📦 Modelo completo preenchido

**[Baixar modelo-iffposter-banner.zip](assets/biblioteca/latex-escrita/modelo-iffposter-banner.zip)** — não é um exemplo fictício: é o pôster real que usei na XIV Mostra do Conhecimento e VII Feira de Oportunidades (IFF-BJI), a mesma pesquisa descrita em [Detecção de Anomalias em Dados do Gaia](pt-br/research/anomaly-detection) — introdução, metodologia, os 4 gráficos reais (diagramas de Kiel, Toomre, Tinsley-Wallerstein, distribuição \[Fe/H]–\[Mg/Fe]), resultados (228 estrelas candidatas a halo) e conclusões, com o cabeçalho oficial do evento e os logos de fomento (FAPERJ/CNPq) inclusos. Compilado e verificado (1 página, sem erros) antes de publicar.

---

## 🔗 Referências e correlatos

- [Aula 09 — Slides com o template oficial do IFFBJI](pt-br/resource/latex/aula-09-slides-beamer)
- [Aula 06 — Classe `ifftese.cls`](pt-br/resource/latex/aula-06-classe-ifftese) — a classe "irmã" para o texto escrito do TCC, com vários padrões em comum.
- [Detecção de Anomalias em Dados do Gaia](pt-br/research/anomaly-detection) — a pesquisa por trás deste pôster.
- [SAB 2025](pt-br/media/2025/sab-2025) e [Escola de Inverno do ON (2026)](pt-br/media/2026/escolainverno-2026) — apresentações em pôster do mesmo trabalho.
- [ReLaTeX — pesquisa por trás da classe `ifftese.cls`](pt-br/research/relatex)
- [Metodologia Científica e Tecnológica](pt-br/resource/engenharia-de-computação/8-periodo/metodologia-cientifica-e-tecnologica)
- [Projeto Final de Curso I](pt-br/resource/engenharia-de-computação/9-periodo/projeto-final-de-curso-i) e [II](pt-br/resource/engenharia-de-computação/10-periodo/projeto-final-de-curso-ii)
- [Curso — visão geral](pt-br/resource/latex)
