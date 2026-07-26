---
publish: true
title: "Aula 09 — Slides de Defesa com Beamer"
created: 2026-07-26
tags:
  - latex
  - escrita
  - recursos
---

> [!note] Resumo
> `beamer` é a classe LaTeX padrão para apresentações em slides — usada aqui para montar os slides de defesa do TCC de exemplo. É um documento **separado** da classe do trabalho escrito ([`ifftese.cls`](pt-br/resource/latex/aula-06-classe-ifftese)): defesa e texto são projetos LaTeX independentes, ainda que compartilhem o mesmo conteúdo de fundo.

**Pré-requisito**: [Aulas 01–05](pt-br/resource/latex) (básico, classes de documento). Recomendado ter visto [Aula 06](pt-br/resource/latex/aula-06-classe-ifftese) para reconhecer as cores/identidade visual reaproveitadas aqui.

**Ver também**: [Aula 10 — Pôster Científico](pt-br/resource/latex/aula-10-poster-cientifico) (o mesmo raciocínio de "resumo visual do trabalho", em formato de banner impresso).

## 1. Por que um documento separado?

Slides de defesa não são "o TCC reformatado" — são um **resumo visual** dele, com muito menos texto por página e ênfase em figuras/gráficos grandes. Por isso, na prática, quase ninguém tenta reaproveitar `ifftese.cls` para os slides: usa-se `\documentclass{beamer}` num arquivo à parte (aqui, `slides.tex`, dentro do [modelo baixável](pt-br/resource/latex/aula-08-pacote-metadados) — Aula 08), copiando manualmente só os poucos dados que os slides realmente precisam (título, autor, orientador, data), sem depender da infraestrutura de metadados da classe do texto.

## 2. Estrutura mínima

```latex
\documentclass[aspectratio=169]{beamer}  % 16:9 — o padrão de projetores/monitores atuais

\usetheme{Madrid}
\usecolortheme{default}

\title[Recomendação de Filmes]{Sistema de Recomendação de Filmes com Filtragem Colaborativa}
\subtitle{Um Estudo de Caso Aplicado ao MovieLens 100K}
\author{Beatriz Andrade Lima}
\institute{Instituto Federal Fluminense --- \textit{Campus} Bom Jesus do Itabapoana}
\date{\today}

\begin{document}

\begin{frame}
  \titlepage
\end{frame}

\begin{frame}{Sumário}
  \tableofcontents
\end{frame}

\end{document}
```

`aspectratio=169` é a opção mais importante a lembrar: sem ela, o Beamer assume 4:3 por padrão — errado para qualquer monitor/projetor atual.

## 3. Temas e cores

`\usetheme{...}` controla o layout geral (cabeçalho, rodapé, barra de navegação); temas comuns: `Madrid`, `Berlin`, `metropolis` (mais minimalista, requer o pacote `beamertheme-metropolis`), `CambridgeUS`. `\usecolortheme{...}` controla só a paleta.

> [!tip] Consistência visual com o TCC escrito
> Para os slides "conversarem" visualmente com o texto, reaproveite as mesmas cores definidas em `ifftese.cls` (Aula 06 §2.3):
> ```latex
> \definecolor{ocre}{RGB}{29,152,66}
> \definecolor{chapterhead}{RGB}{14,69,31}
> \setbeamercolor{structure}{fg=chapterhead}
> \setbeamercolor{title}{fg=white,bg=chapterhead}
> ```

## 4. Frames, blocos e revelação incremental

Cada slide é um ambiente `frame`:

```latex
\begin{frame}{Motivação}
  \begin{itemize}
    \item Catálogos de streaming somam dezenas de milhares de títulos
    \item Nenhum usuário consegue avaliar mais que uma fração mínima
    \pause
    \item[$\Rightarrow$] \alert{como prever o que cada usuário gostaria de ver?}
  \end{itemize}
\end{frame}
```

`\pause` revela os itens um de cada vez ao avançar o slide (útil para não "entregar" a conclusão antes da hora); `\alert{texto}` destaca em cor de ênfase. Três ambientes de caixa prontos para agrupar conteúdo:

```latex
\begin{block}{Definição}
  Filtragem colaborativa prevê o interesse de um usuário a partir do comportamento de outros usuários.
\end{block}

\begin{exampleblock}{Exemplo}
  Um usuário que avaliou bem \textit{Interestelar} e \textit{Chernobyl} provavelmente...
\end{exampleblock}

\begin{alertblock}{Atenção}
  RMSE penaliza erros grandes mais severamente que MAE.
\end{alertblock}
```

## 5. Figuras e tabelas — mais simples que no TCC

Nos slides não existe `\inserirfigura`/`\inserirtabela` (essas macros são específicas de `ifftese.cls`/`macros.sty`) — use `\includegraphics` direto, sem a caixa de legenda/fonte automática:

```latex
\begin{frame}{Arquitetura do sistema}
  \centering
  \includegraphics[width=0.75\textwidth]{img/exemplo-arquitetura.png}
\end{frame}
```

Para tabelas de resultado, prefira menos colunas/linhas do que no texto — um slide não é lugar para uma tabela de 10 linhas.

## 6. Estrutura típica de uma defesa de TCC

Um roteiro que funciona para a maioria das bancas (10–15 minutos de apresentação):

```latex
\section{Introdução}
\begin{frame}{Motivação}...\end{frame}
\begin{frame}{Objetivos}...\end{frame}

\section{Metodologia}
\begin{frame}{Conjunto de dados}...\end{frame}
\begin{frame}{Modelos comparados}...\end{frame}

\section{Resultados}
\begin{frame}{Resultados}...\end{frame}

\section{Conclusão}
\begin{frame}{Considerações finais}...\end{frame}
\begin{frame}{Obrigada!}
  \centering
  \Large Perguntas?
\end{frame}
```

Cada `\section{...}` vira automaticamente uma entrada no sumário (Seção 2) e, se você usar `\AtBeginSection`, pode gerar um "mini-sumário" no início de cada seção mostrando onde a apresentação está:

```latex
\AtBeginSection[]{
  \begin{frame}{Sumário}
    \tableofcontents[currentsection]
  \end{frame}
}
```

## 7. Boas práticas para slides de banca

- **Uma ideia por slide.** Se precisar de dois pontos, são dois slides.
- **Texto grande, pouco texto.** Se cabe ler em silêncio mais rápido do que você fala, tem texto demais.
- **Gráficos grandes, sem legenda minúscula.** O que estava em `\fontsize{10}{12}` no texto vira ilegível projetado — regenere gráficos com fonte maior especificamente para os slides, se precisar.
- **Não leia o slide.** O slide é apoio visual, não o roteiro da sua fala.

## 8. Compilação

```
pdflatex slides.tex
pdflatex slides.tex   % 2ª passada: sumário e numeração de seção
```

Sem bibliografia formal na maioria das apresentações — se precisar citar algo, um `\footnotesize` com a referência resumida no rodapé do próprio slide já resolve.

---

## 🔗 Referências e correlatos

- [`slides.tex` do modelo completo](pt-br/resource/latex/aula-08-pacote-metadados) — o arquivo real, comentado, dentro do `.zip` baixável.
- [Aula 06 — Classe `ifftese.cls`](pt-br/resource/latex/aula-06-classe-ifftese) — origem das cores `ocre`/`chapterhead` reaproveitadas aqui.
- [Aula 10 — Pôster Científico](pt-br/resource/latex/aula-10-poster-cientifico)
- [Documentação oficial do Beamer (CTAN)](https://ctan.org/pkg/beamer)
- [Curso — visão geral](pt-br/resource/latex)
