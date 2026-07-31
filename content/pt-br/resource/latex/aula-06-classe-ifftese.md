---
publish: false
title: "Aula 06 — Anatomia de uma Classe Real: ifftese.cls"
created: 2026-07-26
modified: 2026-07-26T23:54:06.103-03:00
published: 2026-07-26T23:54:06.103-03:00
tags:
  - latex
  - escrita
  - recursos
---

> [!note] Resumo
> Estudo de caso completo de uma classe LaTeX própria — `ifftese.cls` — construída para padronizar TCCs, relatórios técnicos e relatórios científicos do IFF Campus Bom Jesus do Itabapoana segundo a ABNT. Em vez de um exemplo de brinquedo, é a classe que uso de verdade no meu próprio TCC: cada bloco abaixo é código real, comentado configuração por configuração.

**Pré-requisito**: [Aula 05 — Avançado](pt-br/resource/latex/aula-05-avancado) (criar `.cls`/`.sty`, `\makeatletter`, ambientes customizados).

**Ver também**: [Aula 07 — Pacote `macros.sty`](pt-br/resource/latex/aula-07-pacote-macros) (as macros de conteúdo que usam a infraestrutura desta classe) e [Aula 08 — Arquivo `metadados.sty`](pt-br/resource/latex/aula-08-pacote-metadados) (o único arquivo que o estudante de fato edita).

## 0. Arquitetura em três arquivos

A ideia central é separar **engine** de **conteúdo**, para que o estudante nunca precise entender `\makeatletter` para escrever seu trabalho:

| Arquivo | Papel | Quem edita |
|---|---|---|
| `ifftese.cls` | Motor: define todos os comandos, flags, formatação ABNT, floats, cabeçalhos, sumário | Nunca (mantido como "biblioteca") |
| `metadados.sty` | Preenchimento: chama os comandos de metadado definidos pela classe com os dados reais do trabalho | O estudante, uma vez, no início |
| `macros.sty` | Conteúdo: comandos de inserção de figura/tabela/gráfico, ambientes de teorema/exercício, capa, ficha catalográfica | Raramente (só quem estende a classe) |

No documento principal:

```latex
\documentclass{ifftese}
\usepackage{macros}

\aluno{Nome do Estudante}
\titulo{Título do Trabalho}
% ... demais chamadas de metadado (ver Aula 08) ...

\begin{document}
\pretex
\capa
\contracapa
% ... pré-textual ...
\transicaotex
\include{01-intro}
% ...
\transicaopostex
\bibliographystyle{abntex2-alf}
\bibliography{referencias}
\end{document}
```

Note que `ifftese.cls` já faz `\RequirePackage{metadados}` internamente (linha 175) — o arquivo de metadados é carregado automaticamente junto com a classe. Já `macros.sty` precisa de `\usepackage{macros}` explícito no `.tex` principal, por isso o pedido do curso trata os dois **separadamente**.

A classe carrega `article` como base (`\LoadClass[12pt,a4paper]{article}`) e depois reconstrói por cima dela tudo que falta para parecer um documento ABNT completo — inclusive um 4º e 5º nível de seção, já que `article` só tem três.

---

## 1. Bloco A — Fábrica de macros de metadados

O problema que este bloco resolve: uma classe de TCC precisa de **dezenas** de campos de metadado (nome do aluno, orientador, título, banca...). Escrever `\newcommand`/`\newif` manualmente para cada um seria repetitivo e propenso a erro. A solução é uma **fábrica de macros**: três macros genéricas que, dado um nome de campo, geram automaticamente o par "variável interna + comando de atribuição público".

### 1.1 As três fábricas

```latex
\newcommand{\@criarMetadoBase}[2]{%
  \expandafter\gdef\csname tcc@#1\endcsname{#2}% Valor padrão
  \expandafter\gdef\csname #1\endcsname##1{\expandafter\gdef\csname tcc@#1\endcsname{##1}}%
}
```

- **`\@criarMetadoBase{campo}{padrão}`** cria duas coisas: uma variável interna `\tcc@campo` (armazena o valor, começando em `padrão`) e um comando público `\campo{valor}` que o estudante chama em `metadados.sty` para sobrescrevê-la. `\csname...\endcsname` monta o nome do comando dinamicamente a partir da string `campo` — é o que permite `\@criarMetadoBase{titulo}{}` gerar exatamente `\tcc@titulo` e `\titulo{...}` sem repetir código.
- **`\@declararCondicional{flag}{padrão}`** é a mesma ideia, mas para **flags de comportamento** (`sim`/`não`) que serão testadas por `\ifdefstring` em outros pontos da classe. A diferença crítica é o `\edef` em vez de `\gdef`: a flag é **expandida imediatamente** ao ser atribuída, garantindo que `\ifdefstring{\frenteVerso}{sim}{...}` sempre compare uma string literal, nunca uma macro não expandida.
- **`\@declararMetadadoComplexo{campo}{valor-com-comandos}`** é para campos cujo valor padrão **contém outros comandos LaTeX** (ex: `\naturezatrabalho` monta uma frase inteira citando `\tcc@instituicao` e `\tcc@local`). Usa `\gdef` puro (sem `\edef`) para não tentar expandir prematuramente comandos que ainda não têm valor definido — evitando um loop de expansão.

### 1.2 Flags comportamentais (`\@declararCondicional`)

Cada uma controla um comportamento inteiro da classe, testável em qualquer ponto via `\ifdefstring{\tcc@flag}{sim}{...}{...}`:

| Flag | Padrão | Efeito |
|---|---|---|
| `\tipo` | `tcc` | Alterna capa/contracapa/ficha entre 3 estilos: `tcc`, `relatoriocientifico`, `relatoriotecnico` (ver [Aula 07](pt-br/resource/latex/aula-07-pacote-macros)) |
| `\figuracaminho` | `img` | Pasta onde `\inserirfigura` e afins buscam as imagens |
| `\numeracaoPorSecao` | `sim` | Se `sim`, figuras/tabelas/equações numeram como `2.1`, `2.2` (reiniciando a cada seção); se não, numeração contínua |
| `\cabecalho` | `sim` | Liga/desliga o cabeçalho com nome da seção (só página, sem texto, se desligado) |
| `\corlink` | `sim` | Se `sim`, colore os links do sumário/citações (verde citações, vermelho links internos); padrão é invisível (bordas brancas) |
| `\legendacurta` | `sim` | Se `sim`, usa uma legenda curta separada no Sumário/Lista de Figuras; se não, espelha a legenda longa |
| `\sumarioescada` | `sim` | Sumário "em escada" (cada nível mais indentado) vs. linear (todos alinhados) |
| `\frenteVerso` | `sim` | Liga o modo livro (margens espelhadas, capítulos sempre começam em página ímpar) vs. só frente |
| `\capaiff` | `não` | Se `sim`, estampa a imagem de fundo institucional na capa |

### 1.3 Metadados simples (`\@criarMetadoBase`)

Cerca de 60 campos, agrupados por finalidade:

**Autoria e curso**: `aluno`, `abreviaturanome`, `abreviaturanomecompleto`, `email`, `curso`, `areaconcentracao`, `disciplinaFormatada`, `instituicao`, `shortinstituicao`, `siglainstituicao`, `campus`, `local`, `estado`, `estadocompleto`, `ano`.

**Título**: `titulo`, `subtitulo`, `tituloingles`, `subtituloingles`, `shortitulo`, `shortitle`, `palavraschave`, `keywords`.

**Banca examinadora**: `orientador`, `abreviaturaorientador`, `siglainstituicaoorientador`, `coorientador` (+ segundo), `membrobancaum`/`membrobancadois` (+ siglas de instituição de cada um), `dataaprovacao`.

**Coordenação acadêmica (CCSEC)**: `CCSEC`, `siglaccsec`, `ccsecend`, `cepunb`, `ccsectelefone`, `ccsecurl`, `ccsecemail`, `coordccsec`, `diretorgeral`, `diretorensino`, `diretorpesquisa`.

**Relatório técnico/científico** (só relevantes quando `\tipo` ≠ `tcc`): `dadosrelatorio`, `classificacaoseguranca`, `tiporelatorio`, `datarelatorio`, `numeroprojeto`, `resumotexto`, `palavraschavesrel`, `edicao`, `versao`, `numpaginas`, `numclassificacao`, `issn`, `tiragem`, `preco`, `observacoes`.

**Ficha catalográfica**: `tccCodigo`, `tccBiblioteca`, `tccBib`, `tccSistema`, `bolsistas`.

### 1.4 Metadados complexos e derivados (`\@declararMetadadoComplexo`)

Estes são o motivo de existir uma terceira fábrica: seus valores **calculam texto a partir de outros metadados**, então precisam permanecer não-expandidos até o momento de uso.

```latex
\@declararMetadadoComplexo{naturezatrabalho}{%
  Trabalho de Conclusão de Curso apresentado ao \tcc@instituicao\ \textit{Campus}
  \tcc@local\ como requisito parcial para obtenção do título de Bacharel em
  \tcc@areaconcentracao.%
}
```

Isso monta automaticamente a frase-padrão de "natureza do trabalho" que aparece na contracapa e na folha de banca, usando os valores já preenchidos de instituição/local/área — o estudante nunca escreve essa frase manualmente. Existe uma variante `\naturezatrabalhorelatorio` para quando `\tipo` é relatório, e o comando `\tcc@natureza` escolhe entre as duas via `\ifdefstring{\tcc@tipo}{relatorio}{...}{...}`.

Outros derivados na mesma família: `tituloprojeto`/`autores`/`instituicaoexecutora` (espelham `titulo`/`aluno`/`instituicao` por padrão, mas podem ser sobrescritos para relatórios com múltiplos autores/instituições), `tccPaginas` (monta "`\pageref{LastPage}` p. : il.; color, 29,7cm." lendo o contador de páginas final), `tccReferencia` (usa os labels `refInicio`/`refFim` — ver Bloco F — para citar automaticamente o intervalo de páginas das referências), `citacaoautores` e `tccDescritores` (para a ficha catalográfica ABNT).

`\subnivel` é simplesmente um alias de `\tcc@max` (profundidade máxima de seção, padrão 5) — é o que alimenta `secnumdepth`/`tocdepth` no Bloco C.

---

## 2. Bloco B — Pré-âmbulo e pacotes

### 2.1 Abreviações de periódicos de astronomia

Antes mesmo dos pacotes, a classe define ~50 macros como `\aap` → "Astronomy and Astrophysics", `\mnras` → "Monthly Notices of the RAS", `\apj` → "Astrophysical Journal" etc. — a convenção de abreviação de periódicos usada em BibTeX no estilo AASTeX, para bibliografias de astronomia que citam esses nomes por extenso.

### 2.2 Grupos de pacotes (B.1–B.5)

| Grupo | Pacotes principais | Propósito |
|---|---|---|
| B.1 Idioma | `fontenc[T1]`, `babel[brazilian]`, `lipsum` | Acentuação e hifenização em português |
| B.2 Layout | `geometry`, `setspace`, `titlesec`, `titletoc`, `fancyhdr`, `hyphenat[none]`, `changepage`, `eso-pic` | Margens, espaçamento, cabeçalhos, controle fino de hifenização |
| B.3 Conteúdo | `graphicx`, `float`, `subcaption`, `booktabs`, `tikz`, `siunitx`, `listings` | Figuras, tabelas, código, unidades |
| B.4 Links | `xcolor`, `tocloft[titles]`, `hyperref`, `bookmark`, `abntex2cite[alf,...]` | Cores, sumário, hiperlinks, citação ABNT |
| B.5 Utilitários | `datatool`, `refcount` | Bancos de dados ordenáveis (siglas/símbolos/glossário — ver Bloco D) |

### 2.3 `hyperref` com bordas invisíveis por padrão

```latex
\hypersetup{
  colorlinks=false,
  pdfborder={0 0 1},
  citebordercolor={1 1 1}, linkbordercolor={1 1 1},
  urlbordercolor={1 1 1}, filebordercolor={1 1 1}, runbordercolor={1 1 1}
}
```

Em vez de `colorlinks=true` (texto colorido, que a ABNT tradicionalmente reprova), a classe usa **bordas de caixa brancas** — o link existe e funciona, mas é visualmente invisível no PDF impresso. Se `\corlink` for `sim`, um segundo `\hypersetup` troca só duas cores (`citebordercolor`→verde, `linkbordercolor`→vermelho), então o autor pode alternar entre "documento para imprimir" (sem marcação visual) e "documento para revisar na tela" (links visíveis) com uma flag.

### 2.4 `abntex2cite` com opções extensas

`abnt-emphasize=bf`, `abnt-etal-list=4` (a partir de 4 autores, usa "et al."), `abnt-full-initials=yes`, `abnt-repeated-author-omit=yes`/`abnt-repeated-title-omit=yes` (citações consecutivas do mesmo autor/obra usam travessão em vez de repetir), `abnt-doi=doi` — tudo ajustado para bater com a norma ABNT NBR 6023 sem intervenção manual em cada citação.

### 2.5 Listings (B.6) — mapa literal de acentos

```latex
literate={á}{{\'a}}1 {Á}{{\'A}}1 {é}{{\'e}}1 ... {ç}{{\c{c}}}1 {Ç}{{\c{C}}}1
```

O pacote `listings` por padrão não entende UTF-8 dentro de blocos de código; esse mapeamento caractere-a-caractere ensina cada acento/cedilha português a virar o comando LaTeX equivalente. `\lstlistingname` é renomeado para "Algoritmo" (em vez do padrão em inglês "Listing").

### 2.6 Índice remissivo com flag de presença (B.7)

```latex
\let\origindex\index
\renewcommand{\index}{\MarkHasIndex\origindex}
```

Todo `\index{termo}` do documento passa a, silenciosamente, também acionar `\MarkHasIndex` — que grava uma flag booleana no `.aux` (`\global\hasindextrue`, persistida via `\protected@write`). Isso permite que `\imprimirIndice` só imprima a seção "Índice Remissivo" **se pelo menos um `\index` foi de fato usado em algum lugar do documento** — sem isso, documentos sem termos indexados teriam uma seção vazia.

### 2.7 Ajustes tipográficos agressivos (B.8)

`tolerance=1`, `emergencystretch=\maxdimen`, `hyphenpenalty=10000`, `hbadness=10000` — é uma combinação **conflitante de propósito**: `tolerance=1` é extremamente rígido (rejeita quase qualquer espaçamento ruim), mas `emergencystretch` dá ao LaTeX uma "válvula de escape" para esticar linhas em vez de estourar a margem, e `hyphenpenalty=10000` desestimula fortemente a hifenização. Na prática, isso favorece parágrafos com espaçamento ligeiramente mais largo a hifens no meio da palavra ou texto vazando a margem — uma escolha estética deliberada para texto ABNT.

---

## 3. Bloco C — Formatação ABNT

### 3.1 Espaçamento, recuo e `\textsc`

- `\setlength{\parindent}{1.25cm}` — recuo de parágrafo exigido pela ABNT.
- `\setstretch{1.5}` + `\linespread{1.5}` — espaçamento 1,5 entre linhas (a duplicação existe porque `setstretch` só afeta o corpo do texto corrente; `linespread` garante que trocas de fonte dentro do documento herdem o mesmo valor).
- `\renewcommand{\textsc}[1]{\oldtextsc{\small #1}}` — versaletes (`\textsc`) ganham automaticamente um tamanho de fonte menor, porque a implementação padrão de `\textsc` no LaTeX tende a produzir letras visualmente grandes demais quando usada dentro de texto normal.

### 3.2 Um 4º e 5º nível de seção

`article` só define `\section`/`\subsection`/`\subsubsection`. A classe cria os dois níveis que faltam:

```latex
\titleclass{\subsubsubsection}{straight}[\subsubsection]
\newcounter{subsubsubsection}[subsubsection]
\renewcommand{\thesubsubsubsection}{\thesubsubsection.\arabic{subsubsubsection}}
```

`\titleclass{...}{straight}[\subsubsection]` registra o novo nível na hierarquia de `titlesec` como "sequencial" (`straight`) logo abaixo de `\subsubsection`; o contador correspondente é encadeado (`[subsubsection]` reinicia junto com o pai) e `\thesubsubsubsection` monta a numeração `X.Y.Z` por concatenação. O mesmo padrão se repete para o 5º nível, encadeado ao 4º.

### 3.3 Formatação visual por nível

```latex
\titleformat{\section}[hang]{\normalfont\bfseries\fontsize{12}{14}\selectfont}{\thesection}{1em}{\MakeUppercase}
\titleformat{\subsection}[hang]{\normalfont\fontsize{12}{14}\selectfont}{\thesubsection}{1em}{}
\titleformat{\subsubsection}[hang]{\normalfont\slshape\fontsize{12}{14}\selectfont}{\thesubsubsection}{1em}{}
```

Todos os níveis usam a mesma fonte 12pt/14pt (tamanho ABNT-padrão), mas variam em peso/itálico para dar contraste hierárquico: seção em **negrito maiúsculo**, subseção normal, sub-subseção em _itálico_, 4º nível em negrito, 5º nível em negrito-itálico. `\titlespacing*` aplica 12pt de espaço antes/depois em todos os níveis igualmente.

### 3.4 Profundidade dinâmica via `\subnivel`

```latex
\setcounter{secnumdepth}{\numexpr\subnivel\relax}
\setcounter{tocdepth}{\numexpr\subnivel\relax}
```

Como `\subnivel` é alimentado por `\tcc@max` (Bloco A), o autor pode reduzir a profundidade máxima do documento (ex: só numerar até subseção) mudando um único metadado, sem tocar nesta linha.

---

## 4. Bloco D — Floats, listas e ambientes especiais

### 4.1 Seis tipos de float além de figura/tabela

```latex
\newfloat{quadro}{htbp}{loq}     \floatname{quadro}{Quadro}
\newfloat{grafico}{htbp}{lgr}    \floatname{grafico}{Gráfico}
\newfloat{fluxograma}{htbp}{lfl} \floatname{fluxograma}{Fluxograma}
\newfloat{pseudocodigo}{htbp}{lop} \floatname{pseudocodigo}{Pseudocódigo}
\newfloat{saida}{htbp}{loo}      \floatname{saida}{Saída}
\newfloat{algoritmo}{htbp}{loa}  \floatname{algoritmo}{Algoritmo}
```

A ABNT distingue **quadro** (informação textual em grade) de **tabela** (dados numéricos) — algo que o LaTeX puro não modela. Cada `\newfloat` cria um ambiente flutuante completo com sua própria lista (extensão `.loq`, `.lgr` etc.), e `\floatstyle{plaintop}` + `\restylefloat` posiciona a legenda no topo (padrão ABNT) para todos de uma vez.

### 4.2 Legenda dinâmica curta/longa

```latex
\newcommand{\CaptionDinamico}[2]{%
  \ifdefstring{\legendacurta}{sim}{\caption[#2]{#1}}{\caption[#1]{#1}}%
}
```

Se `\legendacurta` for `sim`, a Lista de Figuras usa o texto curto (`#2`) enquanto o corpo do texto mostra o longo (`#1`) — o padrão `\caption[curto]{longo}` nativo do LaTeX. Se não, a lista espelha o texto completo automaticamente, sem precisar passar os dois argumentos toda vez. `\AddContentsDinamico` faz o mesmo para os floats customizados (que não têm um mecanismo nativo de legenda curta, por não serem floats "de verdade" do ponto de vista do `caption`).

### 4.3 Sistema de flags "has-X" (persistência via `.aux`)

```latex
\newif\ifhasfiguras
\newcommand{\MarkHasFiguras}{%
  \global\hasfigurastrue
  \protected@write\@auxout{}{\string\global\string\hasfigurastrue}%
}
```

Um problema clássico de LaTeX: saber, **enquanto compila a primeira página**, se o documento terá alguma figura mais adiante (para decidir se imprime a seção "Lista de Figuras"). A solução clássica é gravar a informação no arquivo `.aux` durante a compilação atual, para que a **próxima** compilação já saiba a resposta desde o início — daí `\protected@write\@auxout` escrevendo `\global\hasfigurastrue` literalmente como texto no `.aux`. Existe uma flag dessas para cada tipo de conteúdo: `hasfiguras`, `hastabelas`, `hasgraficos`, `hasquadros`, `hasfluxogramas`, `hasalgoritmos`, `haspseudocodigos`, `hassaidas`, `hasequationlist`, `hasindex` — cada `\listof...` correspondente só imprime se sua flag estiver ativa.

### 4.4 Siglas e símbolos ordenados dinamicamente (`datatool`)

```latex
\DTLnewdb{siglasdb}
\newcommand{\PrismRegisterSigla}[3]{%
  \DTLnewrow{siglasdb}
  \DTLnewdbentry{siglasdb}{key}{#1}
  \DTLnewdbentry{siglasdb}{sigla}{#2}
  \DTLnewdbentry{siglasdb}{desc}{#3}
}
\newcommand{\addtoSiglas}[3]{%
  \protected@write\@auxout{}{\string\PrismRegisterSigla{\unexpanded{#1}}{\unexpanded{#2}}{\unexpanded{#3}}}%
}
```

Mesma técnica do `.aux` do item anterior, mas para dados estruturados: `\addtoSiglas{chave-de-ordenação}{SIGLA}{Descrição}` no meio do texto grava uma chamada completa a `\PrismRegisterSigla` no `.aux`; na compilação seguinte essa chamada roda e popula um banco de dados `datatool` em memória. `\imprimirSiglas` então roda `\DTLsort{key}{siglasdb}` (ordem alfabética pela chave, não pela ordem de aparição no texto) e itera com `\DTLforeach` imprimindo cada entrada no ambiente `siglas`. O mesmo padrão exato se repete para `\addtoSimbolos`/`\imprimirSimbolos` e para o glossário (`\addtoGlossario`/`\listaGlossario`) — só muda o nome do banco e as colunas.

### 4.5 Listas de alíneas ABNT

```latex
\newlist{alineas}{enumerate}{1}
\setlist[alineas]{label=\alph*), leftmargin=\dimexpr1.25cm+1.25em+\fontdimen2\font\relax, ...}
```

`alineas` (a, b, c...), `subalineas` (travessão –) e `subsubalineas` (marcador •) são três níveis de lista com indentação calculada para bater exatamente com a regra ABNT de recuo de alínea (1,25cm, igual ao recuo de parágrafo) — cada nível soma sua própria largura de rótulo à margem esquerda, para que o texto de todos os níveis fique verticalmente alinhado independente do nível.

---

## 5. Bloco E — Layout de página, recto/verso e sumário

Esta é a parte mais elaborada da classe: implementar a regra ABNT de que **capítulos/seções principais sempre começam em página ímpar (anverso)** quando o documento é frente-e-verso.

### 5.1 Margens que trocam de modo

```latex
\newcommand{\applyTextualMargins}{%
  \ifdefstring{\frenteVerso}{sim}{%
    \newgeometry{inner=3cm,outer=2cm,top=3cm,bottom=2cm,twoside}%
  }{%
    \newgeometry{left=3cm,right=2cm,top=3cm,bottom=2cm}%
  }%
}
\newcommand{\resetMargins}{\restoregeometry}
```

Em modo frente-e-verso, a margem "de dentro" (`inner`, perto da lombada) é sempre maior que a "de fora" (`outer`) — e essas se invertem fisicamente entre páginas pares e ímpares. Em modo só-frente, a distinção não existe e a classe usa margem esquerda/direita fixas.

### 5.2 Forçar início em página ímpar

```latex
\newcommand{\forcarAnverso}{%
  \clearpage
  \ifdefstring{\frenteVerso}{sim}{%
    \ifodd\value{page}\else
      \thispagestyle{empty}\null\clearpage
    \fi
  }{}%
}
```

Depois de um `\clearpage`, se a nova página for **par** (verso), a classe insere uma página em branco (`\null`) com estilo `empty` e avança mais uma vez — garantindo que o próximo conteúdo real caia em página ímpar. Em modo só-frente, isso não faz nada (`{}`).

### 5.3 Seções que se auto-forçam para o anverso

```latex
\newcommand{\enableRectoSections}{%
  \let\origSectionForRecto\section
  \renewcommand{\section}{\@ifstar{\Section@star}{\Section@nostar}}
  \newcommand{\Section@nostar}{\@ifnextchar[{\Section@withopt}{\Section@noopt}}
  \newcommand{\Section@noopt}[1]{\forcarAnverso\origSectionForRecto{##1}}
  ...
}
```

`\section` é redefinido para primeiro rodar `\forcarAnverso` e só então chamar a implementação original salva em `\origSectionForRecto`. O redirecionamento trata as três formas de chamada do LaTeX nativo (`\section{...}`, `\section[...]{...}`, `\section*{...}`) separadamente via `\@ifstar`/`\@ifnextchar`, porque cada uma tem aridade diferente. `\disableRectoSections` simplesmente restaura o `\section` original — usado dentro de anexos/apêndices, que têm sua própria lógica de numeração e não devem herdar esse comportamento.

> [!bug] Bug real encontrado por compilação (corrigido)
> `\listofsaidas` (Bloco D) chamava `\disableRectoSections` no final — sozinha entre todas as `\listofX`, sem nenhuma das outras (`\listoffiguras`, `\listoftables` etc.) fazer o mesmo. Como as listas são impressas no pré-textual, **antes** de `\transicaotex` chamar `\enableRectoSections` pela primeira vez, `\origSectionForRecto` ainda não existe nesse ponto — `\let\section\origSectionForRecto` deixa `\section` efetivamente indefinido para o resto do documento. Sintoma: `! LaTeX Error: Command \section undefined.` bem mais adiante, exatamente em `\transicaotex`. Testado numa compilação real de 3+ passadas (o problema só aparece a partir da 2ª, quando a flag `hassaidas` já existe no `.aux`); a linha estava fora de lugar e foi removida.

### 5.4 Cabeçalhos condicionais (`fancyhdr`)

Dois estilos de página (`textualbar` para o corpo do texto, `posttextualfinal` para pós-textual) cada um com **quatro variações internas**, resultado do produto de duas flags binárias:

| `\cabecalho` | `\frenteVerso` | Comportamento |
|---|---|---|
| sim | sim | Nome da seção ao centro, página alternando direita (ímpar)/esquerda (par) |
| sim | não | Nome da seção ao centro, página sempre à direita |
| não | sim | Sem nome de seção; só número de página, alternando lado |
| não | não | Sem nome de seção; só número de página, sempre à direita |

A sintaxe `\fancyhead[RO]{...}`/`\fancyhead[LE]{...}` do `fancyhdr` (Right-Odd / Left-Even) é o que permite diferenciar página ímpar de página par no mesmo bloco.

### 5.5 "Capítulos" em uma classe sem capítulos

Como a classe herda de `article` (que não tem `\chapter`), quatro comandos preenchem essa lacuna:

- **`\capitulo{Título}`** — título centrado maiúsculo simples, sem entrada no sumário (usado internamente por listas geradas, como "Lista de Figuras").
- **`\capitulosumario{Título}`** — o mesmo visual, mas força página ímpar (`\forcarAnverso`) e adiciona uma entrada **não numerada mas com hyperlink** no sumário, no nível de `section` (usado por "Resumo", "Sumário", "Referências", "Glossário").
- **`\capituloanexo{Título}`** / **`\capituloapendice{Título}`** — os mais elaborados: incrementam seu próprio contador (`anexo`/`apendice`, letras A, B, C...), **zeram todos os contadores de seção e float** (`section`, `figure`, `table`, `grafico`, `quadro`, `equation`, `algoritmo`, `lstlisting`) e redefinem a numeração de todos eles para o formato `A.1`, `B.2.3` etc. Um detalhe sutil: se nenhuma `\section` ainda foi aberta dentro do anexo, o contador de seção está em `0`, o que produziria `A.0.1` — por isso a numeração usa `\ifnum\value{section}>0 \arabic{section}\else 1\fi` para forçar a exibição de `1` nesse caso. Ao final, ambos chamam `\disableRectoSections` (anexos não usam o mecanismo de auto-força de `\section`, já que eles mesmos já forçaram o anverso na abertura) e silenciam o sumário para o conteúdo interno (`\setcounter{tocdepth}{0}` logo depois de registrar a entrada do próprio anexo).

### 5.6 Listas fluidas com coluna de rótulo medida (`\listagemfluida`)

O problema: para alinhar perfeitamente "Figura 2.1 --- Título" com pontilhado e número de página, a coluna do rótulo precisa ter exatamente a largura do **maior rótulo do documento**, não uma largura fixa arbitrária. A solução:

```latex
\newcommand{\listagemfluida}[3]{%
  \begingroup
    \def\numberline##1{\global\setbox\myglobalbox=\hbox{#1~##1~---~}}%
    \sbox0{#2}% roda "no escuro" só para medir
  \endgroup
  \colunalargura=\wd\myglobalbox
  \noindent\begin{tabular*}{\textwidth}{@{}p{\colunalargura}@{}p{\titulolargura}@{}}
    ... & ... \cftdotfill{\cftdotsep} \hb@xt@\@pnumwidth{\hfil #3}
  \end{tabular*}
}
```

O truque é medir o texto do rótulo (`\sbox0{#2}`) **antes** de efetivamente desenhá-lo, guardando a largura resultante numa caixa (`\myglobalbox`); só depois a tabela real é montada usando essa largura medida como definição de coluna. `\AtBeginDocument` troca `\l@figure`/`\l@table`/`\l@quadro`/etc. — os comandos internos que o LaTeX chama para desenhar cada linha das listas de figuras/tabelas — para todos passarem por `\listagemfluida` em vez da implementação padrão do `tocloft`.

### 5.7 Sumário "em escada" vs. linear

Se `\sumarioescada` for `sim`, cada nível de seção no sumário recebe uma indentação progressiva (calculada a partir da largura real dos números "99.99.9" etc., via `\settowidth`) — visual de "escada" onde subseções ficam visualmente aninhadas sob suas seções-pai. Se não, todos os níveis alinham à mesma margem esquerda (`\sumariosecshift` etc. todos zerados) — um sumário "linear" mais compacto, comum em relatórios curtos.

---

## 6. Bloco F — Bibliografia

```latex
\renewenvironment{thebibliography}[1]{%
  \label{refInicio}
  \capitulosumario{\bibname}
  \list{...}{%
    \setlength{\itemsep}{\baselineskip}% um espaço simples entre referências
    \setlength{\parsep}{0pt}%
  }%
  \sloppy
  \label{refFim}
}{\endlist}
```

Os labels `refInicio`/`refFim`, colocados logo no início e no fim do ambiente, são o que permite `\tccReferencia` (Bloco A) citar automaticamente "p. X a Y" na ficha catalográfica sem o autor precisar digitar manualmente o intervalo de páginas — ele muda a cada compilação conforme o texto cresce, e os labels sempre apontam para o valor certo. `\tableofcontents` também é redefinido aqui para usar `\capitulo{Sumário}` e restaurar a profundidade completa antes de `\@starttoc{toc}`.

---

## 🔗 Referências e correlatos

- [Aula 05 — Avançado](pt-br/resource/latex/aula-05-avancado) — os fundamentos (`.sty`/`.cls`, `\makeatletter`) que esta aula assume conhecidos.
- [Aula 07 — Pacote `macros.sty`](pt-br/resource/latex/aula-07-pacote-macros) — as macros de conteúdo (capa, figuras, ambientes de teorema) construídas sobre esta classe.
- [Aula 08 — Arquivo `metadados.sty`](pt-br/resource/latex/aula-08-pacote-metadados) — o arquivo que o estudante de fato preenche.
- [Curso — visão geral](pt-br/resource/latex)
- [Guia de classes (LaTeX Project)](https://www.latex-project.org/help/documentation/clsguide.pdf)
- [Documentação do `abntex2cite`](https://www.abntex.net.br) — a base normativa (ABNT NBR 6023) por trás das opções de citação usadas no Bloco B.
- [Metodologia Científica e Tecnológica](pt-br/resource/engenharia-de-computação/8-periodo/metodologia-cientifica-e-tecnologica) — onde essas normas ABNT viram obrigação de fato.
- [Projeto Final de Curso I](pt-br/resource/engenharia-de-computação/9-periodo/projeto-final-de-curso-i) e [II](pt-br/resource/engenharia-de-computação/10-periodo/projeto-final-de-curso-ii) — o TCC que esta classe formata.
- [ReLaTeX — pesquisa por trás desta classe](pt-br/research/relatex)
