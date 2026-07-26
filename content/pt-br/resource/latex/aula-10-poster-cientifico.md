---
publish: true
title: "Aula 10 — Pôster Científico (Banner)"
created: 2026-07-26
tags:
  - latex
  - escrita
  - recursos
---

> [!note] Resumo
> Um pôster acadêmico é um documento de **página única e grande** (tipicamente A0), pensado para ser lido a 1–2 metros de distância num corredor de congresso — não é o TCC nem os slides "espremidos" numa folha. Aqui usamos `tikzposter`, a opção mais simples de configurar entre os pacotes de pôster do LaTeX.

**Pré-requisito**: [Aula 09 — Slides com Beamer](pt-br/resource/latex/aula-09-slides-beamer) (mesma lógica de "resumo visual do trabalho", formato diferente).

## 1. Três pacotes possíveis, uma recomendação

| Pacote | Base | Quando usar |
|---|---|---|
| `tikzposter` | Independente (usa TikZ internamente) | **Recomendado** — mais simples de configurar, blocos e colunas prontos, tema visual coerente sem esforço |
| `beamerposter` | Estende `beamer` | Se você já conhece bem Beamer e quer reaproveitar comandos dele |
| `a0poster` | Classe genérica, baixo nível | Controle total, mas você monta o layout (colunas, caixas) manualmente com `minipage`/`tikz` |

Este curso usa `tikzposter` — é o que está no [modelo baixável](pt-br/resource/latex/aula-08-pacote-metadados) (`banner.tex`).

## 2. Estrutura mínima

```latex
\documentclass[25pt, a0paper, portrait, margin=0mm, innermargin=15mm,
               blockverticalspace=15mm, colspace=15mm, subcolspace=8mm]{tikzposter}

\usetheme{Default}
\usecolorstyle{Australia}   % paleta pronta — troque à vontade

\title{Sistema de Recomendação de Filmes com Filtragem Colaborativa}
\author{Beatriz Andrade Lima --- Orientador: Prof. Dr. Ricardo Nunes Barbosa}
\institute{Instituto Federal Fluminense --- \textit{Campus} Bom Jesus do Itabapoana}

\begin{document}
\maketitle

\begin{columns}
  \column{0.5}
    \block{Introdução}{Texto curto...}
    \block{Metodologia}{Texto curto...}
  \column{0.5}
    \block{Resultados}{Texto curto...}
    \block{Conclusão}{Texto curto...}
\end{columns}

\end{document}
```

`a0paper` + `portrait` é o par mais comum exigido por editais de congresso (confira sempre o tamanho pedido — alguns pedem `landscape` ou `a1paper`). `25pt` é o tamanho de fonte base — grande de propósito, porque o documento inteiro vai ser impresso em ~84×119cm.

> [!warning] Cuidado com `\author{A \and B}`
> `\and` é o separador oficial do `tikzposter`/`beamer` para múltiplos autores lado a lado — mas, testado por compilação real neste curso, combiná-lo com **qualquer `tabular` normal** em um bloco mais adiante no pôster quebra a compilação com `! Misplaced \crcr.` bem longe do `\author`, direto na tabela seguinte. Um único `\author{Nome A --- Orientador: Nome B}` (texto corrido, sem `\and`) evita o problema por completo e ainda fica legível. Se seu pôster realmente precisa de vários autores em colunas, teste isolado antes de adicionar tabelas.

## 3. Blocos e colunas

`\block{Título}{conteúdo}` é a unidade básica — uma caixa com cabeçalho colorido. `\begin{columns}...\end{columns}` divide o pôster em colunas independentes, cada uma recebendo seus próprios blocos empilhados verticalmente; `\column{0.5}` define a largura relativa (aqui, metade). Para subdividir uma coluna em duas menores lado a lado, existe `\begin{subcolumns}...\subcolumn{...}{...}\end{subcolumns}` dentro de uma coluna.

## 4. Tema e cores

`\usetheme{Default}` controla forma/estilo geral dos blocos; `\usecolorstyle{Australia}` (ou `Denmark`, `Spain`, `Autumn`, entre outras) troca só a paleta. Para reaproveitar as cores do TCC escrito (mesmo raciocínio da Aula 09 §3):

```latex
\definecolorstyle{ifftese}{
  \definecolor{colorOne}{RGB}{29,152,66}   % ocre
  \definecolor{colorTwo}{RGB}{14,69,31}    % chapterhead
  \definecolor{colorThree}{RGB}{240,244,250}
}{
  \colorlet{backgroundcolor}{white}
  \colorlet{framecolor}{colorTwo}
  \colorlet{titlefgcolor}{white}
  \colorlet{titlebgcolor}{colorTwo}
  \colorlet{blocktitlebgcolor}{colorOne}
  \colorlet{blocktitlefgcolor}{white}
  \colorlet{blockbodybgcolor}{colorThree}
}
\usecolorstyle{ifftese}
```

## 5. Estrutura típica de conteúdo

Um pôster de congresso raramente foge desta receita:

```
┌─────────────────────────────────────────────┐
│   TÍTULO — Autores — Instituição/afiliação   │
├───────────────────┬───────────────────────────┤
│ Introdução/Objetivo│         Resultados         │
│                    │   (gráficos GRANDES aqui)  │
│    Metodologia     │                             │
│                    │        Conclusão            │
│                    │  Referências · Contato/QR   │
└───────────────────┴───────────────────────────┘
```

- **Introdução/Objetivo**: 3–5 linhas, não um resumo completo.
- **Metodologia**: um diagrama vale mais que um parágrafo aqui.
- **Resultados**: a parte que deve dominar visualmente o pôster — gráficos grandes, tabela curta.
- **Conclusão**: 2–3 bullets, não um parágrafo de "considerações finais".
- **Referências**: 3–5 no máximo, fonte pequena — não é o lugar para a lista completa do TCC.

```latex
\block{Resultados}{
  \begin{tikzfigure}[Comparação de RMSE entre os modelos avaliados]
    \includegraphics[width=0.9\linewidth]{img/exemplo-arquitetura.png}
  \end{tikzfigure}
}
```

`\begin{tikzfigure}[legenda]...\end{tikzfigure}` é o equivalente do `tikzposter` a uma figura com legenda — não confundir com `\inserirfigura` (essa é exclusiva de `ifftese.cls`/`macros.sty`, Aula 07).

## 6. QR code para o trabalho completo (opcional)

Um pôster tem espaço limitado — um QR code levando ao TCC completo, ao repositório do código, ou a este próprio site é comum:

```latex
\usepackage{qrcode}
...
\block{Saiba mais}{
  \qrcode[height=3cm]{https://exemplo.com/tcc-completo.pdf}
}
```

## 7. Boas práticas de pôster

- **Legível a 1,5m de distância.** Se você precisa se aproximar da tela para ler seu próprio rascunho, o texto está pequeno demais.
- **Hierarquia visual clara.** Título do pôster > títulos de bloco > corpo de texto — três tamanhos de fonte bem diferentes, não uma gradação sutil.
- **Menos texto do que parece necessário.** Quem para na frente do seu pôster vai conversar com você — o pôster é gancho, não o artigo inteiro.

## 8. Compilação

```
pdflatex banner.tex
```

Documentos A0 demoram mais para compilar e para abrir no visualizador de PDF do que um documento normal — isso é esperado, não é erro. Para conferir o layout rapidamente sem esperar a impressão em tamanho real, reduza a visualização do PDF para ~10% no seu leitor, ou gere um preview em `a4paper` temporariamente trocando só essa opção da classe (lembre de voltar para `a0paper` antes de enviar para impressão).

---

## 🔗 Referências e correlatos

- [`banner.tex` do modelo completo](pt-br/resource/latex/aula-08-pacote-metadados) — o arquivo real, comentado, dentro do `.zip` baixável.
- [Aula 09 — Slides com Beamer](pt-br/resource/latex/aula-09-slides-beamer)
- [Aula 06 — Classe `ifftese.cls`](pt-br/resource/latex/aula-06-classe-ifftese) — origem das cores reaproveitadas na paleta customizada.
- [Documentação do `tikzposter` (CTAN)](https://ctan.org/pkg/tikzposter)
- [Curso — visão geral](pt-br/resource/latex)
