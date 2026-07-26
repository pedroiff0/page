---
publish: true
title: "Aula 07 — Pacote de Conteúdo: macros.sty"
created: 2026-07-26
tags:
  - latex
  - escrita
  - recursos
---

> [!note] Resumo
> A segunda peça do trio: `macros.sty` é onde moram os comandos de **conteúdo** — capa, ficha catalográfica, inserção de figuras/tabelas/gráficos, ambientes de teorema/exercício com sistema de resposta cruzada — construídos sobre a infraestrutura de metadados e flags definida em [`ifftese.cls`](pt-br/resource/latex/aula-06-classe-ifftese).

**Pré-requisito**: [Aula 06 — Classe `ifftese.cls`](pt-br/resource/latex/aula-06-classe-ifftese) (flags `\tcc@*`, sistema de floats customizados, `\CaptionDinamico`).

Carregado explicitamente no documento principal, depois do `\documentclass`:

```latex
\documentclass{ifftese}
\usepackage{macros}
```

## 1. Texto e citação

| Comando | Uso |
|---|---|
| `\comentario{texto}` | Anotação visível em teal — `[nome: texto]` — para revisão colaborativa, nunca deve sobrar na versão final |
| `\link{url}{texto}` | Atalho para `\href` com cor teal fixa |
| `\lombada[largura]` | Gera o texto da lombada (nome, título, ano) rotacionado -90° dentro de uma caixa — para encadernação |
| `\citacaoTCC` | Monta a citação bibliográfica por extenso do próprio trabalho (autor, título, natureza, curso, instituição, ano) a partir dos metadados já preenchidos — usado, por exemplo, no topo da [Errata](#5-errata) |
| `citacaolonga` (ambiente) | Bloco de citação direta longa (ABNT: recuo 4cm, fonte 10pt, espaçamento simples) |

## 2. Pré-textuais: capa, contracapa e ficha catalográfica

### 2.1 `\pretex`

Executado logo após `\begin{document}`: liga a numeração arábica de páginas, mas com `\pagestyle{empty}` (sem exibir número) e `\hypersetup{pageanchor=false}` (evita que links do PDF apontem para essas páginas iniciais antes delas terem uma identidade de página estável) — o padrão ABNT de que a capa/folha de rosto contam para a paginação mas não a exibem.

### 2.2 `\capa` — três layouts em um comando

`\capa` inspeciona `\tcc@tipo` e ramifica entre dois desenhos visuais completamente diferentes:

```latex
\newcommand{\capa}[1][]{%
  #1%
  \IfStrEq{\tcc@tipo}{relatoriotecnico}{%
    % ESTILO 1: capa de relatório técnico — instituição, campus, curso, depois
    % espaço, CEP, número do relatório, ISSN, título, classificação de segurança
  }{%
    % ESTILOS 2 e 3 (TCC / relatório científico): instituição, campus, curso,
    % nome do aluno, título, local/estado/ano — e, se \capaiff=sim, estampa
    % a imagem de fundo institucional via \AddToShipoutPictureBG*
  }
}
```

O argumento opcional `#1` permite passar redefinições locais entre colchetes (ex: `\capa[\renewcommand{\tcc@titulo}{Outro título}]`) sem alterar o metadado globalmente — útil para gerar uma segunda capa alternativa no mesmo documento. Cada linha de texto só aparece **se o metadado correspondente não estiver vazio** (`\IfStrEq{\tcc@campo}{}{}{...texto...}`), incluindo a lógica de só inserir quebra de linha (`\\`) entre dois campos se **ambos** estiverem preenchidos — evitando linhas em branco fantasmas quando um campo opcional é deixado vazio.

### 2.3 `\contracapa`

Mesma ramificação por `\tipo`, mas com o bloco de **natureza do trabalho + orientação** centralizado (`\tcc@natureza`, herdado do Bloco A da classe) e, no caso de relatório técnico, um bloco extra com volume/ISSN/classificação de segurança.

### 2.4 Ficha catalográfica

Dois comandos irmãos:

- **`\fichacatalograficaimg{arquivo.pdf}`** — quando a biblioteca já forneceu uma ficha pronta em PDF (gerada pelo sistema da biblioteca), simplesmente inclui a primeira página com `\includepdf`, zerando o contador de página (`\addtocounter{page}{-1}`) para ela não contar na numeração visível.
- **`\fichacatalografica[redefinições]`** — quando não há PDF pronto, **desenha a ficha do zero**: uma tabela com código de catalogação, autoria, título, orientadores (lista com `\settowidth` medindo a largura do rótulo "Orientadores:" ou "Professor(a):" para alinhar múltiplas linhas de orientação), curso, referência de páginas e descritores — todos os campos vindo de `\tcc@tcc*` (Bloco A). Ramifica internamente para o estilo "Equipe Técnica" quando `\tipo=relatoriotecnico` (coordenador, pesquisadores, bolsistas em vez de orientador/banca).

### 2.5 Errata

```latex
\newcommand{\errata}[1]{%
  \capitulo{Errata}
  \noindent\citacaoTCC
  \begin{tabular}{|c|c|p{6cm}|p{6cm}|}
    \hline \textbf{Folha} & \textbf{Linha} & \textbf{Onde se lê} & \textbf{Leia-se} \\ \hline
    #1
  \end{tabular}
}
```

Recebe as linhas da tabela como argumento livre — o autor escreve `\errata{1 & 5 & erro & correção \\}` e a macro monta o cabeçalho da tabela e a citação por extenso do trabalho (via `\citacaoTCC`) automaticamente.

### 2.6 Banca examinadora

`\banca[...]` desenha nome do aluno, título, natureza do trabalho, data de aprovação e uma linha de assinatura (régua + nome + sigla de instituição) para **cada** membro presente — orientador, até dois coorientadores, até dois membros de banca — pulando silenciosamente qualquer um cujo metadado esteja vazio, então uma banca de 3 pessoas não deixa três linhas de assinatura em branco.

### 2.7 `\identificacao` (ficha de identificação técnica)

Uma tabela de metadados "crua", pensada para relatórios técnicos/científicos que a instituição exige em formato de formulário — 4 colunas alternando entre campos de TCC (curso/ano/aluno) e de relatório (projeto/número/autores), sempre escolhendo o conjunto certo via `\IfStrEq{\tcc@tipo}{relatorio}{...}{...}`.

## 3. Dedicatória, agradecimentos, epígrafe, resumo

```latex
\newenvironment{epigrafe}{%
  \vspace*{\fill}\begin{flushright}\begin{minipage}{0.6\textwidth}\begin{flushright}
}{%
  \end{flushright}\end{minipage}\end{flushright}
}
\newcommand{\itemepigrafe}[2]{\textit{"#1"} \\ -- {#2} \\}
```

`\dedicatoria{texto}` e o ambiente `epigrafe` seguem o mesmo padrão visual ABNT (bloco alinhado à direita, empurrado para o rodapé da página com `\vspace*{\fill}`) — a diferença é que uma epígrafe pode ter **várias** citações (`\itemepigrafe` chamado repetidamente dentro do ambiente), cada uma com texto e autor.

`\resumo{texto}{palavras-chave}` e `\abstractabnt{texto}{keywords}` fazem dupla função: imprimem o texto do resumo/abstract **e** salvam as palavras-chave nas variáveis globais `\palavraschave`/`\keywords` (usadas depois na ficha catalográfica e nos metadados do PDF), então o autor só digita a lista de palavras-chave uma vez.

## 4. Transições estruturais

| Comando | Efeito |
|---|---|
| `\transicaotex` | Início do corpo textual: `\cleardoublepage`, ativa `\enableRectoSections`, aplica margens textuais, religa âncoras de página do `hyperref`, muda para o estilo de página `textualbar` |
| `\transicaopostex` | Fim do corpo textual: muda para o estilo `posttextualfinal` (usado por referências, anexos, glossário) |
| `\imprimirListas` | Chama, em sequência, **todas** as listas condicionais da classe (figuras, gráficos, fluxogramas, equações, algoritmos, pseudocódigos, saídas, quadros, tabelas, siglas, símbolos) — cada uma só imprime de fato se sua flag "has-X" (Aula 06, §4.3) estiver ativa |
| `\imprimirglossario` / `\indices` | Atalhos para `\listaGlossario`/`\imprimirIndice` (Bloco D/B.7 da classe) |
| `\teseinfo` | Frase de colofão ("Este trabalho foi escrito usando LaTeX na classe `ifftese`...") — texto de rodapé automático que documenta a própria ferramenta usada |

## 5. Inserção de figuras, tabelas e gráficos

Este é o bloco mais extenso do pacote: uma família de comandos que **encapsulam em uma linha** tudo que normalmente exigiria um ambiente `figure`/`table` completo — centralização, legenda dinâmica (curta/longa, Aula 06 §4.2), label, marcação da flag "has-X" (Aula 06 §4.3) e uma linha de "Fonte:" alinhada exatamente com a largura do conteúdo inserido.

### 5.1 O padrão comum: medir, depois alinhar a fonte

```latex
\newcommand{\inserirfigura}[6][]{%
  \begin{figure}[H]
    \MarkHasFiguras \centering \CaptionDinamico{#3}{#4} \label{#6}%
    \sbox{\inserirbox}{\includegraphics[#1]{\figuracaminho/ #2}}%
    \makebox[\linewidth][c]{\usebox{\inserirbox}}%
    \setlength{\lastinserirwidth}{\wd\inserirbox}%
    \noindent\makebox[\linewidth][c]{\makebox[\wd\inserirbox][l]{\fontsize{10}{12}\selectfont Fonte: #5}}%
  \end{figure}
}
```

Argumentos: `[opções-includegraphics] arquivo legenda-longa legenda-curta fonte label`. A imagem é primeiro desenhada dentro de uma **caixa invisível** (`\sbox{\inserirbox}{...}`) só para medir sua largura final (`\wd\inserirbox`) — só depois ela é de fato exibida centralizada, e a linha "Fonte:" reusa exatamente essa largura medida como ponto de alinhamento à esquerda. É o mesmo truque de medição usado por `\listagemfluida` (Aula 06 §5.6), aplicado a imagens em vez de rótulos de lista.

### 5.2 Variantes por número de subfiguras e orientação

| Comando | Layout |
|---|---|
| `\inserirtabela` / `\inserirtabelaL` | Tabela com `adjustbox`/`resizebox` automático se ultrapassar `\textwidth` |
| `\inserirquadro` | Mesmo padrão, mas no float `quadro` (não `table`) |
| `\inserirDuasSubfiguras(L)`, `\inserirTresSubfiguras(L)`, `\inserirQuatroSubfiguras(L)` | 2/3/4 imagens lado a lado sob uma legenda única, com numeração de subfigura própria (`\thesubgrafico` = `\thegrafico` + letra) |
| `\inserirgrafico` + `\inserirDuasSubgraficos(L)`/`\inserirTresSubgraficosL`/`\inserirQuatroSubgraficos(L)` | Equivalente para o float `grafico` |
| `\inserirfluxograma` | Para o float `fluxograma` |
| `\inserirelementografico` | Versão genérica que recebe o **nome do ambiente flutuante** como argumento — usada quando nenhuma das macros específicas serve |

O sufixo `L` (`...L`) marca a variante que recebe a **largura final já calculada manualmente** (`\setlength{\lastinserirwidth}{#N}`) em vez de medi-la automaticamente — útil quando o conteúdo não é uma imagem simples (ex: dois `\includegraphics` lado a lado montados à mão) e a medição automática por `\sbox` não seria confiável.

## 6. Blocos de código especiais

`\algoritmocaption`, `\pseudocodocaption` e `\saidacaption` desenham o cabeçalho centralizado ("**Algoritmo 3** --- Título") de um bloco `lstlisting` que usa os estilos `latex`/`saidaoutput`/`saidaoutputsmall` (definidos em Aula 06 §2.5), incrementam o contador do float correspondente e marcam sua flag "has-X" — para blocos de código que não são, tecnicamente, floats do LaTeX (um `lstlisting` simples), mas precisam se comportar como se fossem para efeito de numeração e lista.

## 7. Destaque de valores com unidades

```latex
\newcommand{\destaque}[2]{\fbox{\ensuremath{\SI{#1}{#2}}}}
\newcommand{\destaqueC}[2]{\begin{center}\fbox{\ensuremath{\displaystyle\SI{#1}{#2}}}\end{center}}
```

Atalho para `\SI` (do `siunitx`) dentro de uma caixa — útil para destacar um resultado numérico com unidade (ex: `\destaque{6.7}{\percent}`) em linha ou centralizado em bloco.

## 8. Notas de rodapé customizadas

```latex
\let\oldfootnote\footnote
\renewcommand{\footnote}[1]{\oldtextsc\footnote{\setstretch{1.0}\fontsize{10}{12}\selectfont #1}}
```

**Toda** chamada de `\footnote` no documento passa a forçar espaçamento simples e fonte 10pt/12pt — sem o autor precisar lembrar disso em cada nota. `\notarodape{texto}` é um atalho que já adiciona o ponto final. `\notasemmarcador{texto}` usa o ambiente `NoHyper` para inserir uma nota **sem número/marcador visível** (usado, por exemplo, para o colofão `\teseinfo` — uma nota de rodapé "solta" na primeira página, sem um asterisco ou número associado a ela).

## 9. Ambientes pedagógicos: teoremas, exercícios e caixas

A última seção do arquivo é uma biblioteca de ambientes de estilo "livro-texto", construída sobre `mdframed` — pensada para materiais didáticos (como os das aulas 01–08 deste próprio curso!) mais do que para o TCC em si.

### 9.1 Caixas visuais (`mdframed`)

| Caixa | Cor de fundo | Uso típico |
|---|---|---|
| `tBox` | cinza claro, borda preta | Teorema, conjectura, resposta |
| `problemBox` / `problemBoxBorder` | cinza / branco com borda | Problema, desafio |
| `exampleBox` | cinza claro | Exemplo |
| `defBox` | cinza claro | Definição |
| `atencaoBox` | amarelo | Atenção |
| `importanteBox` | vermelho claro | Importante |
| `saibaMaisBox` | azul claro | Saiba mais |
| `theoBox`/`lemmaBox`/`axiomBox`/`corolBox`/`propBox`/`conjBox`/`demoBox` | cinza claro, **podem quebrar página** (`splittopskip`/`splitbottomskip=0pt`) | Teorema/Lema/Axioma/Corolário/Proposição/Conjectura/Demonstração longos |
| `resolucaoBox` | cinza claro | Resolução de exercício/problema/desafio |

A distinção entre as caixas "normais" (`nobreak=true`, nunca quebram de página — podem deixar espaço em branco no fim da página anterior) e as `theoBox`/`lemmaBox`/etc. (podem quebrar) existe porque teoremas e demonstrações tendem a ser mais longos que cabe numa página, enquanto definições/exemplos curtos ficam visualmente melhores sem quebra no meio.

### 9.2 Ambientes de teorema com numeração condicional

```latex
\ifdefstring{\numeracaoPorSecao}{sim}{%
  \newtheorem{definitionT}{Definição}[section]
  ...
}{%
  \newtheorem{definitionT}{Definição}
  ...
}
```

Todo o catálogo de ambientes (`definicao`, `teorema`, `lema`, `proposicao`, `axioma`, `corolario`, `exemplo`, `observacao`) é declarado **duas vezes**, dependendo de `\numeracaoPorSecao` (a mesma flag da classe, Aula 06 §1.2) — se `sim`, cada um numera por seção (`3.1`, `3.2`); se não, numeração contínua no documento inteiro.

### 9.3 Problema/Exercício/Desafio com resposta cruzada

O sistema mais elaborado do arquivo: um problema pode ser **referenciado a partir da sua própria resposta**, e a resposta linka de volta ao enunciado — sem o autor gerenciar labels manualmente em dois lugares.

```latex
\newcommand{\problemlabellink}[1]{%
  \gdef\nexproblemlabel{#1}
  \global\hasproblemlabeltrue
}
\renewenvironment{problem}[1][]{%
  \refstepcounter{problem}%
  \ifhasproblemlabel\phantomsection\label{\nexproblemlabel}\fi%
  \noindent\textbf{Problema \theproblem\ #1}%
  \ifhasproblemlabel\hfill\hyperref[ans:\nexproblemlabel]{\(\square\)}\global\hasproblemlabelfalse\fi%
}{\end{problemBox}}

\newenvironment{resolucaoTo}[1]{%
  ...
}
\newenvironment{resolucao}[1]{%
  \phantomsection\label{res:#1}\label{ans:#1}%
  ...\hyperref[#1]{Resolução~\ref*{#1}}...
}
```

Fluxo de uso: `\problemlabellink{prob:3}` antes de `\begin{problem}` grava o label pendente; o ambiente `problem` o consome, cria o `\label` e desenha um quadradinho clicável (`\hyperref[ans:prob:3]{□}`) que pula direto para a resolução. Do outro lado, `\begin{resolucao}{prob:3}` cria simultaneamente os labels `res:prob:3` e `ans:prob:3`, e detecta automaticamente (via `\IfBeginWith`) se o label começa com `des:`/`prob:`/`ex:` para escrever "Resolução do Desafio"/"do Problema"/"do Exercício" corretamente — só a partir do prefixo da string do label, sem argumento extra. O mesmo padrão (`desafiolabellink`/`exerciselabellink`) se repete para desafios e exercícios.

---

## 🔗 Referências e correlatos

- [Aula 06 — Classe `ifftese.cls`](pt-br/resource/latex/aula-06-classe-ifftese) — a base de flags, floats e metadados sobre a qual este pacote é construído.
- [Aula 08 — Arquivo `metadados.sty`](pt-br/resource/latex/aula-08-pacote-metadados) — onde os metadados usados por `\capa`, `\contracapa` e `\fichacatalografica` são de fato preenchidos.
- [Curso — visão geral](pt-br/resource/latex)
- [Documentação do `mdframed`](https://ctan.org/pkg/mdframed) e do [`datatool`](https://ctan.org/pkg/datatool) (CTAN).
