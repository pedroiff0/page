---
publish: false
title: "Aula 11 — Relatório Corporativo"
created: 2026-07-31
modified: 2026-07-31
tags:
  - latex
  - escrita
  - recursos
  - corporativo
---

> [!note] Resumo
> Construção da classe `relatoriocorp.cls`, do zero: um relatório de consultoria/empresa com identidade visual própria — paleta de marca em um único ponto de troca, capa com faixa colorida, cabeçalho e rodapé com logo, página de controle de versões, sumário executivo em destaque, tabelas financeiras alinhadas na vírgula decimal, gráficos com a cor da marca, caixas de recomendação/risco, marca d'água de confidencialidade e página de assinaturas. É a mesma engenharia da [Aula 06](pt-br/resource/latex/aula-06-classe-ifftese) (`ifftese.cls`), mas com o alvo trocado: em vez de cumprir a ABNT, cumprir um manual de marca.

**Pré-requisito**: [Aulas 01–05](pt-br/resource/latex) — em especial a [Aula 05](pt-br/resource/latex/aula-05-avancado), que introduz `.cls`/`.sty` e `\makeatletter`. Ter visto a [Aula 06](pt-br/resource/latex/aula-06-classe-ifftese) ajuda, mas não é obrigatório.

**Ver também**: [Aula 12 — Slides Corporativos](pt-br/resource/latex/aula-12-slides-corporativos), que aplica exatamente esta paleta a um tema Beamer, e [Modelos Corporativos](pt-br/resource/latex/modelos-corporativos), que junta os dois num projeto só.

## 0. O que muda de um trabalho acadêmico para um relatório corporativo

Um TCC tem uma norma pública para obedecer (ABNT NBR 14724) e um leitor que **precisa** ler o documento inteiro. Um relatório corporativo tem o oposto dos dois:

| | Acadêmico (`ifftese.cls`) | Corporativo (`relatoriocorp.cls`) |
|---|---|---|
| Autoridade da forma | norma externa (ABNT) | manual de marca do cliente |
| Leitor típico | banca, lê tudo | diretoria, lê 2 páginas |
| Elemento mais importante | fundamentação e método | sumário executivo e recomendação |
| Tipografia | serifada, sóbria, preto | sans-serif, cor da marca |
| Ciclo de vida | uma entrega final | versionado, revisado, aprovado |
| Confidencialidade | público por definição | quase sempre restrito |

Isso tem consequência direta no projeto da classe: a paleta precisa ser trocável em um lugar só (cada cliente tem a sua), o documento precisa carregar **metadados de processo** (versão, autor, aprovador, data de revisão) e o sumário executivo precisa ser visualmente impossível de ignorar.

## 1. Esqueleto da classe

```latex
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{relatoriocorp}[2026/07/31 v1.0 Relatorio corporativo com identidade visual]

% Flags de comportamento, no mesmo espírito de \frenteVerso/\capaiff da Aula 06:
% ligadas por opção de classe, consultadas depois no corpo do arquivo.
\newif\if@confidencial \@confidencialfalse
\newif\if@semlogo      \@semlogofalse

\DeclareOption{confidencial}{\@confidencialtrue}
\DeclareOption{semlogo}{\@semlogotrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax

\LoadClass[11pt,a4paper]{article}
```

`article` e não `report`: relatório corporativo raramente tem capítulo — tem seção numerada e anexo. `\DeclareOption*` repassa qualquer opção desconhecida (`12pt`, `oneside`, `draft`) para `article`, então a classe não precisa conhecer de antemão todas as opções possíveis.

Uso:

```latex
\documentclass[confidencial]{relatoriocorp}
```

## 2. A paleta — o único ponto de troca de marca

```latex
\RequirePackage[table,svgnames]{xcolor}

\definecolor{corpPrimaria}{HTML}{123B5C}   % institucional, títulos e capa
\definecolor{corpSecundaria}{HTML}{2E9E8F} % apoio, réguas e destaques positivos
\definecolor{corpDestaque}{HTML}{E8A33D}   % atenção, riscos, ressalvas
\definecolor{corpTexto}{HTML}{1C1C1C}      % corpo de texto (nunca preto puro)
\definecolor{corpCinza}{HTML}{6B7280}      % metadados, legendas, rodapé
\definecolor{corpFundo}{HTML}{F4F6F8}      % fundo de caixas e linhas zebradas
```

> [!warning] `xcolor` tem que ser carregado aqui, e com `table`
> A opção `table` é o que habilita `\rowcolors` (usada nas tabelas do §9). Se um pacote posterior carregar `xcolor` sem ela, o LaTeX aborta com **"Option clash for package xcolor"**. Carregar cedo, dentro da classe, resolve de uma vez: quem vier depois recebe o pacote já carregado com as opções certas.

Seis cores, um lugar. Trocar a marca do documento inteiro — capa, títulos, gráficos, caixas, rodapé — é editar estas seis linhas. Se o cliente entregar cores em CMYK, `\definecolor{corpPrimaria}{cmyk}{0.85,0.55,0.25,0.35}` funciona igual; se entregar em RGB 0–255, use `{RGB}{18,59,92}`.

**Uma nota de acessibilidade que vale a pena respeitar**: `corpTexto` é quase preto, não preto (`#000`). Texto preto puro sobre branco puro tem contraste alto demais e cansa em leitura longa — é por isso que praticamente todo manual de marca sério especifica um "preto de texto" levemente lavado.

## 3. Tipografia sans-serif

```latex
\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}
\RequirePackage[brazil]{babel}
\RequirePackage{lmodern}
\RequirePackage[scaled=0.92]{helvet}
\renewcommand{\familydefault}{\sfdefault}
\RequirePackage{microtype}

\color{corpTexto}
```

Documento corporativo é sans-serif por convenção (é o que os manuais de marca pedem, herdado do design de apresentação). `helvet` com `scaled=0.92` compensa o fato de a Helvetica/Nimbus ter altura-x maior que a Computer Modern — sem o `scaled`, o texto parece grande demais ao lado das fórmulas e números.

Para usar **a fonte real da marca** (quase sempre uma OpenType comprada ou do Google Fonts), troque o motor para LuaLaTeX ou XeLaTeX e este bloco por:

```latex
% Compilar com lualatex/xelatex; sem inputenc e sem fontenc.
\RequirePackage{fontspec}
\setsansfont{Inter}[Scale=MatchLowercase, Numbers=Lining]
\setmainfont{Inter}[Scale=MatchLowercase]
\renewcommand{\familydefault}{\sfdefault}
```

`Numbers=Lining` importa mais do que parece em relatório: sem ele, muitas fontes usam algarismos de estilo antigo (com descendentes), que ficam desalinhados dentro de tabelas financeiras.

## 4. Geometria, cabeçalho e rodapé com logo

```latex
\RequirePackage[a4paper, top=3.2cm, bottom=2.6cm, left=2.5cm, right=2.5cm,
                headheight=30pt, headsep=16pt, footskip=22pt]{geometry}
\RequirePackage{fancyhdr}
\RequirePackage{graphicx}
\RequirePackage{lastpage}

% Metadados usados no cabeçalho/rodapé e na capa (§5).
\newcommand{\corplogo}{}
\newcommand{\corpcliente}{}
\newcommand{\corpprojeto}{}
\newcommand{\logomarca}[1]{\renewcommand{\corplogo}{#1}}
\newcommand{\cliente}[1]{\renewcommand{\corpcliente}{#1}}
\newcommand{\projeto}[1]{\renewcommand{\corpprojeto}{#1}}

\fancypagestyle{corp}{%
  \fancyhf{}
  \fancyhead[L]{\footnotesize\color{corpCinza}\corpprojeto}
  \fancyhead[R]{\if@semlogo\else\ifx\corplogo\empty\else
                  \includegraphics[height=20pt]{\corplogo}\fi\fi}
  \fancyfoot[L]{\footnotesize\color{corpCinza}\corpcliente}
  \fancyfoot[R]{\footnotesize\color{corpCinza}\thepage\ de \pageref{LastPage}}
  \renewcommand{\headrulewidth}{0.8pt}
  \renewcommand{\footrulewidth}{0.4pt}
  \renewcommand{\headrule}{{\color{corpPrimaria}%
      \hrule height \headrulewidth width \headwidth}}
  \renewcommand{\footrule}{{\color{corpCinza!50}%
      \hrule height \footrulewidth width \headwidth}}
}
\pagestyle{corp}
```

Três detalhes que causam dor de cabeça se ignorados:

- **`headheight=30pt`**. O padrão do `geometry` é ~12pt, e um logo de 20pt não cabe — o LaTeX emite `\headheight is too small` e o cabeçalho invade o texto. Se você trocar a altura do logo, ajuste aqui junto.
- **`\headrule` colorido precisa das chaves duplas**. `{{\color{...}\hrule ...}}` — sem o grupo interno, a cor vaza para o resto da página. É o mesmo motivo pelo qual `\footrule` está escrito assim.
- **`\pageref{LastPage}` exige duas compilações**. Na primeira passada o rodapé mostra "1 de ??".

`\ifx\corplogo\empty` é o teste padrão de "esta macro está vazia?": funciona porque `\corplogo` foi declarada com corpo vazio, exatamente como `\empty`. Sem esse teste, um documento sem logo quebraria no `\includegraphics{}`.

## 5. A capa

```latex
\RequirePackage{tikz}
\usetikzlibrary{calc}

\newcommand{\corptitulo}{Título do relatório}
\newcommand{\corpsubtitulo}{}
\newcommand{\corpversao}{v1.0}
\newcommand{\corpdata}{\today}
\newcommand{\corpautor}{}

\renewcommand{\title}[1]{\renewcommand{\corptitulo}{#1}}
\newcommand{\subtitulo}[1]{\renewcommand{\corpsubtitulo}{#1}}
\newcommand{\versao}[1]{\renewcommand{\corpversao}{#1}}
\renewcommand{\author}[1]{\renewcommand{\corpautor}{#1}}
\renewcommand{\date}[1]{\renewcommand{\corpdata}{#1}}

\newcommand{\capacorp}{%
  \begin{titlepage}
  \thispagestyle{empty}
  \begin{tikzpicture}[remember picture, overlay]
    % Faixa institucional cobrindo o terço superior da página.
    \fill[corpPrimaria]
      (current page.north west) rectangle ([yshift=-10cm]current page.north east);
    \fill[corpSecundaria]
      ([yshift=-10cm]current page.north west)
      rectangle ([yshift=-10.35cm]current page.north east);

    % Título e subtítulo, dentro da faixa.
    \node[anchor=north west, text width=14cm, align=left]
      at ([shift={(2.5cm,-3.4cm)}]current page.north west) {%
        \color{white}\fontsize{30}{34}\selectfont\bfseries\corptitulo\par
        \vspace{0.45cm}
        \color{white!80}\fontsize{15}{19}\selectfont\mdseries\corpsubtitulo};

    % Bloco de metadados, no rodapé da capa.
    \node[anchor=south west, text width=14cm, align=left]
      at ([shift={(2.5cm,3.0cm)}]current page.south west) {%
        \color{corpCinza}\footnotesize
        \textbf{\color{corpPrimaria}Cliente}\quad\corpcliente\par\vspace{2pt}
        \textbf{\color{corpPrimaria}Projeto}\quad\corpprojeto\par\vspace{2pt}
        \textbf{\color{corpPrimaria}Autoria}\quad\corpautor\par\vspace{2pt}
        \textbf{\color{corpPrimaria}Versão}\quad\corpversao\ \textbullet\ \corpdata};

    % Logo, canto inferior direito.
    \if@semlogo\else\ifx\corplogo\empty\else
      \node[anchor=south east]
        at ([shift={(-2.5cm,3.0cm)}]current page.south east)
        {\includegraphics[height=1.6cm]{\corplogo}};
    \fi\fi

    \if@confidencial
      \node[anchor=south west, font=\footnotesize\bfseries, text=corpDestaque]
        at ([shift={(2.5cm,1.8cm)}]current page.south west)
        {DOCUMENTO CONFIDENCIAL — DISTRIBUIÇÃO RESTRITA};
    \fi
  \end{tikzpicture}
  \end{titlepage}
}
```

`remember picture, overlay` é o que permite ancorar em `current page.north west` e desenhar **fora** da caixa de texto, sangrando até a borda do papel. Custo: o TikZ precisa das posições absolutas gravadas no `.aux`, então **a capa só fica certa a partir da segunda compilação** (na primeira, tudo se amontoa no canto).

Repare que `\title`/`\author`/`\date` foram *redefinidos* em vez de criados com nomes novos: quem já escreve LaTeX espera esses comandos, e não há `\maketitle` padrão aqui para conflitar.

## 6. Controle do documento — histórico de revisões

Página que não existe em trabalho acadêmico e é obrigatória em quase todo relatório entregue a cliente: quem escreveu, quem revisou, quem aprovou, o que mudou entre as versões.

```latex
\RequirePackage{tabularx}
\RequirePackage{booktabs}
\RequirePackage{array}

\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}

\newenvironment{historico}{%
  \section*{Controle do documento}
  \rowcolors{2}{corpFundo}{white}%
  \begin{tabularx}{\linewidth}{@{}l l L{3.4cm} X@{}}
  \toprule
  \rowcolor{white}
  \textbf{Versão} & \textbf{Data} & \textbf{Autoria} & \textbf{Alterações} \\
  \midrule
}{%
  \bottomrule
  \end{tabularx}
  \par\vspace{1em}
}
```

Uso:

```latex
\begin{historico}
  v0.1 & 12/06/2026 & P. Andrade  & Versão inicial para revisão interna. \\
  v0.9 & 28/06/2026 & P. Andrade  & Inclui análise de sensibilidade (§4). \\
  v1.0 & 05/07/2026 & Comitê      & Aprovada para envio ao cliente. \\
\end{historico}
```

`\rowcolors{2}{corpFundo}{white}` zebra a partir da segunda linha; o `\rowcolor{white}` explícito na linha de cabeçalho a protege da contagem. `L{3.4cm}` é a coluna de largura fixa alinhada à esquerda (sem ela, `p{}` justifica e abre buracos em coluna estreita) e `X` é a coluna elástica do `tabularx`, que absorve a largura que sobrar.

## 7. Sumário executivo

```latex
\RequirePackage[most]{tcolorbox}

\newtcolorbox{sumarioexec}{%
  enhanced, breakable,
  colback=corpFundo, colframe=corpPrimaria,
  boxrule=0pt, leftrule=4pt, arc=2pt,
  left=12pt, right=12pt, top=10pt, bottom=10pt,
  title={Sumário executivo},
  fonttitle=\bfseries\large, coltitle=white, colbacktitle=corpPrimaria
}
```

`breakable` é o detalhe que importa: sem ele, um sumário executivo que passe de uma página estoura silenciosamente para fora da margem inferior. `leftrule=4pt` com `boxrule=0pt` dá a barra lateral colorida sem moldura fechada — o visual "callout" que todo relatório moderno usa.

> [!tip] Escreva o sumário executivo por último e limite-o a uma página
> A regra prática de consultoria: se o diretor ler **só** esta caixa, ele tem que saber o problema, o que foi feito, o resultado e a decisão pedida. Todo o resto do relatório é evidência para essa página.

## 8. Títulos de seção com a cor da marca

```latex
\RequirePackage{titlesec}

\titleformat{\section}
  {\color{corpPrimaria}\Large\bfseries}{\thesection}{0.7em}{}
  [{\color{corpSecundaria}\titlerule[1.2pt]}]
\titleformat{\subsection}
  {\color{corpPrimaria}\large\bfseries}{\thesubsection}{0.6em}{}
\titleformat{\subsubsection}
  {\color{corpCinza}\normalsize\bfseries}{\thesubsubsection}{0.5em}{}

\titlespacing*{\section}   {0pt}{2.4ex plus 1ex minus .2ex}{1.4ex plus .2ex}
\titlespacing*{\subsection}{0pt}{2.0ex plus .8ex minus .2ex}{0.9ex plus .2ex}
```

O sexto argumento de `\titleformat` (entre colchetes) é o material *depois* do título — é ali que entra a régua fina abaixo de cada `\section`. Os valores `plus/minus` no `\titlespacing` são cola elástica: dão ao LaTeX margem de manobra para fechar as páginas sem viúvas, algo que espaçamento rígido impede.

Sumário no mesmo tom:

```latex
\RequirePackage{tocloft}
\renewcommand{\cftsecfont}{\bfseries\color{corpPrimaria}}
\renewcommand{\cftsecpagefont}{\bfseries\color{corpPrimaria}}
\renewcommand{\cftsecleader}{\color{corpCinza!40}\cftdotfill{\cftdotsep}}
```

## 9. Tabelas financeiras

O problema clássico: uma coluna de valores em que os números não alinham na vírgula fica ilegível. `siunitx` resolve com a coluna `S`.

```latex
\RequirePackage{siunitx}
\sisetup{
  output-decimal-marker = {,},
  group-separator = {.},
  group-minimum-digits = 4,
  table-format = 7.2,
  table-number-alignment = center
}
\RequirePackage{caption}
\captionsetup{font=small, labelfont={bf,color=corpPrimaria}, labelsep=period}
```

```latex
\begin{table}[htbp]
  \centering
  \caption{Receita por linha de produto (em milhares de reais)}
  \label{tab:receita}
  \rowcolors{2}{corpFundo}{white}
  \begin{tabularx}{\linewidth}{@{}X S S S@{}}
    \toprule
    \rowcolor{white}
    \textbf{Linha de produto} & {\textbf{Q1}} & {\textbf{Q2}} & {\textbf{Q3}} \\
    \midrule
    Assinaturas    & 1240.50 & 1388.20 & 1502.75 \\
    Serviços       &  830.00 &  795.40 &  910.10 \\
    Licenciamento  &  412.25 &  455.60 &  470.00 \\
    \midrule
    \rowcolor{white}
    \textbf{Total} & 2482.75 & 2639.20 & 2882.85 \\
    \bottomrule
  \end{tabularx}
\end{table}
```

> [!warning] Cabeçalho de coluna `S` precisa de chaves
> `{\textbf{Q1}}` e não `\textbf{Q1}`. A coluna `S` tenta interpretar o conteúdo como número; texto solto ali gera erro ou alinhamento errado. As chaves dizem ao `siunitx` "isto é texto, centralize e não analise".

Três regras de tabela que separam um relatório profissional de um amador, todas herdadas do `booktabs`: **nunca use linhas verticais**, use apenas `\toprule`/`\midrule`/`\bottomrule`, e nunca `\hline` duplo. Espaço branco separa colunas melhor que régua.

## 10. Gráficos com a paleta da marca

```latex
\RequirePackage{pgfplots}
\pgfplotsset{compat=1.18}

\pgfplotsset{
  corpbar/.style={
    ybar, bar width=16pt,
    width=\linewidth, height=6.2cm,
    ymajorgrids, grid style={corpCinza!25},
    axis line style={corpCinza!60},
    tick label style={font=\small, color=corpCinza},
    label style={font=\small, color=corpTexto},
    legend style={draw=none, font=\small, at={(0.5,-0.20)},
                  anchor=north, legend columns=-1},
    every axis plot/.append style={draw=none},
    nodes near coords,
    every node near coord/.append style={font=\scriptsize, color=corpCinza},
    ymin=0, enlarge x limits=0.18,
  }
}
```

```latex
\begin{figure}[htbp]
  \centering
  \begin{tikzpicture}
    \begin{axis}[corpbar,
        symbolic x coords={Q1,Q2,Q3},
        xtick=data,
        ylabel={Receita (R\$ mil)}]
      \addplot+[fill=corpPrimaria]   coordinates {(Q1,1240) (Q2,1388) (Q3,1503)};
      \addplot+[fill=corpSecundaria] coordinates {(Q1,830) (Q2,795) (Q3,910)};
      \legend{Assinaturas, Serviços}
    \end{axis}
  \end{tikzpicture}
  \caption{Evolução trimestral da receita por linha de produto.}
  \label{fig:receita}
\end{figure}
```

Ganho real de fazer o gráfico em LaTeX em vez de colar um PNG do Excel: a fonte é a mesma do texto, o vetor não pixela em nenhuma ampliação, e a cor sai literalmente da mesma variável `corpPrimaria` que pinta a capa. Quando o cliente trocar a paleta, o gráfico troca junto.

> [!tip] Gráfico pesado? Externalize
> Com muitos gráficos, cada compilação fica lenta. `\usetikzlibrary{external}\tikzexternalize` compila cada figura uma vez e reaproveita o PDF nas próximas rodadas.

## 11. Caixas de recomendação, risco e KPI

```latex
\newtcolorbox{recomendacao}[1][Recomendação]{%
  enhanced, breakable, colback=corpSecundaria!8, colframe=corpSecundaria,
  boxrule=0pt, leftrule=4pt, arc=2pt, left=10pt, right=10pt,
  title={#1}, fonttitle=\bfseries, coltitle=white, colbacktitle=corpSecundaria}

\newtcolorbox{risco}[1][Risco]{%
  enhanced, breakable, colback=corpDestaque!10, colframe=corpDestaque,
  boxrule=0pt, leftrule=4pt, arc=2pt, left=10pt, right=10pt,
  title={#1}, fonttitle=\bfseries, coltitle=white, colbacktitle=corpDestaque}

% Cartão de indicador: \kpi[cor]{valor}{rótulo}
\newcommand{\kpi}[3][corpPrimaria]{%
  \begin{tcolorbox}[enhanced, colback=white, colframe=#1, boxrule=1pt,
                    arc=4pt, halign=center, valign=center, height=2.7cm,
                    left=4pt, right=4pt]
    {\color{#1}\fontsize{25}{27}\selectfont\bfseries #2}\par\vspace{3pt}
    {\footnotesize\color{corpCinza} #3}
  \end{tcolorbox}}
```

Uma fileira de indicadores, com altura igualada automaticamente:

```latex
\begin{tcbraster}[raster columns=3, raster equal height,
                  raster column skip=8pt, raster row skip=8pt]
  \kpi{+16,1\%}{Crescimento de receita YoY}
  \kpi[corpSecundaria]{R\$ 2,88 mi}{Receita no Q3}
  \kpi[corpDestaque]{34 dias}{Prazo médio de recebimento}
\end{tcbraster}
```

`tcbraster` (da biblioteca `raster`, incluída no `[most]`) é o que evita a gambiarra de `minipage` com altura chutada: `raster equal height` mede a caixa mais alta e iguala todas.

## 12. Marca d'água de confidencialidade

```latex
\RequirePackage{eso-pic}

\if@confidencial
  \AddToShipoutPictureBG{%
    \begin{tikzpicture}[remember picture, overlay]
      \node[rotate=54, scale=6.5, text opacity=0.06,
            text=corpPrimaria, font=\bfseries]
        at (current page.center) {CONFIDENCIAL};
    \end{tikzpicture}}
\fi
```

`\AddToShipoutPictureBG` carimba **atrás** do conteúdo, em todas as páginas — o `BG` importa: no *foreground* (`\AddToShipoutPictureFG`) a marca d'água cobriria os links clicáveis. Opacidade de 6% é o limite prático: visível na tela e na impressão, sem atrapalhar a leitura.

Alternativa pronta, se você não quiser controlar o TikZ: `\usepackage{draftwatermark}` com `\SetWatermarkText{CONFIDENCIAL}` e `\SetWatermarkLightness{0.94}`.

## 13. Página de assinaturas

```latex
\newcommand{\linhaassinatura}[2]{%
  \parbox[t]{0.44\linewidth}{\centering
    \vspace{1.6cm}\rule{\linewidth}{0.4pt}\par\vspace{3pt}
    \textbf{#1}\par{\footnotesize\color{corpCinza}#2}}}

\newcommand{\aprovacoes}[1]{%
  \section*{Aprovações}
  \noindent Este documento foi revisado e aprovado pelas partes abaixo.
  \par\vspace{0.6cm}
  #1
  \par\vspace{0.8cm}
  {\footnotesize\color{corpCinza}
   Emitido em \corpdata\ — versão \corpversao.\par}}
```

```latex
\aprovacoes{%
  \linhaassinatura{Pedro H. R. de Andrade}{Autoria — Analista responsável}
  \hfill
  \linhaassinatura{Nome do Aprovador}{Diretoria de Operações}}
```

`\parbox[t]` com `\hfill` entre os dois é o que mantém as linhas alinhadas pelo topo e distribuídas na largura — `minipage` faria o mesmo, mas `\parbox` é mais curto para conteúdo de um parágrafo.

## 14. `main.tex` completo

```latex
\documentclass[confidencial]{relatoriocorp}

\logomarca{figuras/logo-cliente.pdf}
\cliente{Indústria Exemplo S.A.}
\projeto{Diagnóstico de eficiência operacional}
\title{Diagnóstico de Eficiência Operacional}
\subtitulo{Análise do ciclo produtivo e recomendações de curto prazo}
\author{Pedro H. R. de Andrade}
\versao{v1.0}
\date{31 de julho de 2026}

\begin{document}

\capacorp

\begin{historico}
  v0.1 & 12/06/2026 & P. Andrade & Versão inicial para revisão interna. \\
  v1.0 & 31/07/2026 & Comitê     & Aprovada para envio ao cliente. \\
\end{historico}

\begin{sumarioexec}
  A operação apresenta ociosidade média de 18\% no turno da tarde,
  concentrada em duas linhas. A recomendação central é o remanejamento
  de turno descrito na Seção~\ref{sec:recomendacoes}, com retorno
  estimado em dois trimestres.
\end{sumarioexec}

\tableofcontents
\clearpage

\section{Contexto e escopo}
Texto.

\section{Método}
Texto.

\section{Resultados}
Ver Tabela~\ref{tab:receita} e Figura~\ref{fig:receita}.

\section{Recomendações}\label{sec:recomendacoes}

\begin{recomendacao}
  Remanejar duas equipes do turno da tarde para o turno da manhã.
\end{recomendacao}

\begin{risco}[Risco de implantação]
  A mudança depende de renegociação de escala com o sindicato.
\end{risco}

\appendix
\section{Memória de cálculo}
Texto.

\aprovacoes{%
  \linhaassinatura{Pedro H. R. de Andrade}{Autoria}
  \hfill
  \linhaassinatura{Nome do Aprovador}{Diretoria de Operações}}

\end{document}
```

Compile com `latexmk -pdf main.tex` — ele resolve sozinho as **três** passadas que este documento precisa (TikZ `remember picture`, `\pageref{LastPage}` e o sumário).

## 15. Erros comuns

| Sintoma | Causa | Correção |
|---|---|---|
| `Option clash for package xcolor` | outro pacote carregou `xcolor` sem `table` | carregar `xcolor` cedo, na classe (§2) |
| Capa amontoada no canto | primeira compilação, `.aux` ainda vazio | compilar de novo (ou usar `latexmk`) |
| `\headheight is too small` | logo mais alto que o cabeçalho | aumentar `headheight` no `geometry` (§4) |
| Rodapé mostra "1 de ??" | `lastpage` precisa de duas passadas | compilar de novo |
| Números desalinhados na tabela | coluna comum em vez de `S` | usar `S` e chavear os cabeçalhos (§9) |
| Cor vazando após uma régua | `\color` fora de grupo | envolver em chaves: `{{\color{...}...}}` |
| Caixa estourando a margem inferior | `tcolorbox` sem `breakable` | acrescentar `breakable` (§7) |

## 🔗 Referências e correlatos

- [Aula 12 — Slides Corporativos](pt-br/resource/latex/aula-12-slides-corporativos) — a mesma paleta aplicada a um tema Beamer.
- [Modelos Corporativos](pt-br/resource/latex/modelos-corporativos) — estrutura de pastas, troca de marca e checklist de entrega.
- [Aula 06 — Classe `ifftese.cls`](pt-br/resource/latex/aula-06-classe-ifftese) — a mesma engenharia de classe, com a ABNT no lugar do manual de marca.
- [Aula 05 — Avançado](pt-br/resource/latex/aula-05-avancado) — `.cls`/`.sty`, `\makeatletter` e opções de classe.
- [ReLaTeX](pt-br/research/relatex) — a pesquisa por trás dessas classes.
- [Documentação do `tcolorbox`](https://ctan.org/pkg/tcolorbox) — o pacote mais útil deste material; vale ler a seção de `enhanced`.
- [Manual do `pgfplots`](https://ctan.org/pkg/pgfplots) e [do `siunitx`](https://ctan.org/pkg/siunitx).
- [Documentação do `booktabs`](https://ctan.org/pkg/booktabs) — as regras de tabela do §9 estão argumentadas lá.
