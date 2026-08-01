---
publish: false
title: Modelos Corporativos
created: 2026-07-31
modified: 2026-07-31
tags:
  - latex
  - escrita
  - recursos
  - corporativo
---

> [!note] Resumo
> A parte prática da trilha corporativa: como organizar um projeto que gera **relatório e apresentação a partir da mesma marca**, trocar a identidade visual em três passos, compilar sem sofrer e conferir a entrega antes de mandar para o cliente. Os dois modelos são construídos, linha a linha, na [Aula 11](pt-br/resource/latex/aula-11-relatorio-corporativo) e na [Aula 12](pt-br/resource/latex/aula-12-slides-corporativos) — esta página é o que fica aberto ao lado enquanto você usa.

## Qual modelo usar

| Você precisa de… | Use | Construído em |
|---|---|---|
| Relatório, diagnóstico, parecer, proposta | `relatoriocorp.cls` | [Aula 11](pt-br/resource/latex/aula-11-relatorio-corporativo) |
| Apresentação de resultado, comitê, pitch | `beamerthemecorp.sty` | [Aula 12](pt-br/resource/latex/aula-12-slides-corporativos) |
| TCC, dissertação (ABNT / IFF) | `ifftese.cls` | [Aula 06](pt-br/resource/latex/aula-06-classe-ifftese) |
| Slides de defesa no IFF-BJI | `slidesiffmodelo.cls` | [Aula 09](pt-br/resource/latex/aula-09-slides-beamer) |
| Pôster científico no IFF-BJI | `iffposter.cls` | [Aula 10](pt-br/resource/latex/aula-10-poster-cientifico) |
| Um documento simples, sem identidade visual | `article`/`report` puro | [Modelos de Documento](pt-br/resource/latex/modelos-de-documento) |

## Estrutura do projeto

Um cliente, uma pasta, os dois documentos dividindo a mesma marca:

```
cliente-exemplo/
├── marca.sty                 ← paleta, logo e fonte: fonte única de verdade
├── relatoriocorp.cls         ← classe do relatório (Aula 11)
├── beamerthemecorp.sty       ← tema dos slides (Aula 12)
├── relatorio.tex
├── apresentacao.tex
├── conteudo/
│   ├── 01-contexto.tex
│   ├── 02-metodo.tex
│   └── 03-recomendacoes.tex
├── figuras/
│   ├── logo-cliente.pdf
│   └── grafico-receita.pdf
├── dados/
│   └── receita.csv
├── referencias.bib
└── latexmkrc
```

## O truque que faz os dois casarem: `marca.sty`

Nas Aulas 11 e 12, cada arquivo define a própria paleta — didático, mas duplicado. Num projeto real, extraia as cores para um pacote só, carregado pelos dois:

```latex
% marca.sty
\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{marca}[2026/07/31 Identidade visual do cliente]

\RequirePackage[table,svgnames]{xcolor}

\definecolor{corpPrimaria}{HTML}{123B5C}
\definecolor{corpSecundaria}{HTML}{2E9E8F}
\definecolor{corpDestaque}{HTML}{E8A33D}
\definecolor{corpTexto}{HTML}{1C1C1C}
\definecolor{corpCinza}{HTML}{6B7280}
\definecolor{corpFundo}{HTML}{F4F6F8}

\newcommand{\marcaLogo}{figuras/logo-cliente.pdf}
\newcommand{\marcaNome}{Indústria Exemplo S.A.}
```

Depois, em `relatoriocorp.cls` e em `beamerthemecorp.sty`, troque o bloco de `\definecolor` por uma linha:

```latex
\RequirePackage{marca}
```

Pronto: relatório e slides passam a ser **fisicamente incapazes** de divergir de cor. Esse é o mesmo raciocínio de `metadados.sty` na [Aula 08](pt-br/resource/latex/aula-08-pacote-metadados) — separar "o que muda a cada trabalho" de "o que nunca muda".

## Trocar a marca em três passos

1. **Cores.** Edite os seis `\definecolor` de `marca.sty`. Se o manual do cliente der CMYK, use `{cmyk}{c,m,y,k}`; se der RGB 0–255, `{RGB}{18,59,92}`; hexadecimal é `{HTML}{123B5C}` (sem o `#`).
2. **Logo.** Substitua `figuras/logo-cliente.pdf`. **Prefira PDF ou SVG convertido para PDF** — logo em PNG serrilha na impressão e na projeção. Se só houver PNG, exija pelo menos 300 dpi no tamanho final de uso.
3. **Fonte.** Se a marca tem fonte própria, troque o motor para LuaLaTeX e use `fontspec` (receita na [Aula 11 §3](pt-br/resource/latex/aula-11-relatorio-corporativo)). Sem a fonte licenciada em mãos, fique na Helvetica/Nimbus do `helvet` — é neutra e não gera problema de licença.

> [!tip] Peça o manual de marca antes de começar
> Quase toda empresa tem um PDF de *brand guidelines* com paleta em CMYK/RGB/HEX, versões do logo (positivo, negativo, monocromático) e área de respiro mínima. Vinte minutos lendo esse arquivo economizam três rodadas de revisão estética.

## Compilar sem sofrer

Os dois modelos precisam de **duas a três passadas** (TikZ com `remember picture`, `\pageref{LastPage}`, sumário, `\inserttotalframenumber`). Deixe o `latexmk` cuidar disso:

```
# latexmkrc
$pdf_mode = 1;          # pdflatex; use 4 para lualatex
$out_dir  = 'build';
$clean_ext = 'bbl nav snm run.xml synctex.gz';
```

```bash
latexmk -pdf relatorio.tex        # compila o que for preciso
latexmk -pdf -pvc apresentacao.tex  # recompila a cada save
latexmk -C                        # limpa tudo
```

No **Overleaf**, suba a pasta inteira como projeto, marque `relatorio.tex` como documento principal em *Menu → Main document* e troque o compilador para LuaLaTeX em *Menu → Compiler* se você tiver ido pelo caminho do `fontspec`.

> [!warning] O `.cls` e o `.sty` precisam estar na mesma pasta do `.tex`
> Ou instalados na sua árvore TeX local (`~/texmf/tex/latex/`). O erro `File 'relatoriocorp.cls' not found` é quase sempre isso — não um problema de instalação do LaTeX.

## Versionar em Git sem dor

Documento corporativo é revisado várias vezes, muitas vezes por mais de uma pessoa. Duas convenções resolvem 90% dos conflitos:

- **Uma frase por linha.** Quebre o parágrafo no `.tex` a cada ponto final. O LaTeX ignora a quebra simples, e o `git diff` passa a mostrar a frase alterada em vez de repintar o parágrafo inteiro.
- **`build/` no `.gitignore`.** Junto de `*.aux`, `*.log`, `*.out`, `*.nav`, `*.snm`, `*.toc`, `*.synctex.gz`. O PDF final: versione **só** as versões entregues, com o número no nome (`relatorio-v1.0.pdf`).

E mantenha a tabela do ambiente `historico` (Aula 11 §6) alinhada com as tags do repositório — é o que permite responder "o que mudou da v0.9 para a v1.0?" sem abrir dois PDFs lado a lado.

## Checklist antes de entregar

- [ ] Compilou **do zero** (`latexmk -C && latexmk -pdf`) sem erro e sem `Overfull \hbox` gritante.
- [ ] Sumário, referências cruzadas e paginação corretos — sinal de que as passadas todas rodaram.
- [ ] Nenhum `??` sobrou no texto (referência quebrada) e nenhum "Lorem ipsum" ou dado de exemplo.
- [ ] Versão e data na capa batem com a última linha do histórico de revisões.
- [ ] Marca d'água de confidencialidade ligada (ou deliberadamente desligada).
- [ ] Logo em vetor, sem serrilhado ao ampliar para 400%.
- [ ] Fontes embutidas no PDF: `pdffonts relatorio.pdf` — toda linha deve mostrar `emb yes`.
- [ ] Metadados do PDF preenchidos (não "main.tex" no título da janela):

```latex
\usepackage[pdfusetitle]{hyperref}
\hypersetup{
  pdftitle={Diagnóstico de Eficiência Operacional},
  pdfauthor={Pedro H. R. de Andrade},
  pdfsubject={Relatório de diagnóstico — v1.0},
  pdfkeywords={eficiência operacional, diagnóstico},
  colorlinks=true, linkcolor=corpPrimaria,
  urlcolor=corpSecundaria, citecolor=corpPrimaria
}
```

- [ ] Nome do arquivo entregue no padrão `cliente-documento-vX.Y.pdf`.

## 🔗 Referências e correlatos

- [Aula 11 — Relatório Corporativo](pt-br/resource/latex/aula-11-relatorio-corporativo)
- [Aula 12 — Slides Corporativos](pt-br/resource/latex/aula-12-slides-corporativos)
- [Modelos de Documento](pt-br/resource/latex/modelos-de-documento) — os equivalentes genéricos e acadêmicos.
- [Aula 08 — `metadados.sty`](pt-br/resource/latex/aula-08-pacote-metadados) — o mesmo padrão de "um arquivo só para o que muda".
- [ReLaTeX](pt-br/research/relatex) — a pesquisa que originou esta forma de montar classes.
- [Curso — visão geral](pt-br/resource/latex)
